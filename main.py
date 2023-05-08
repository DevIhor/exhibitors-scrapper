import time
from typing import Iterator, Dict

import core.settings
from core import write_data, prepare_writer, get_companies
from core.chatgpt import get_chatgpt_response
from core.google import search as google_search

from core.nlp import extract_names, gen_decision_maker_request, get_linkedin_search_request, \
	get_alternative_search_request
from scrappers.techspodenver import scrape as scrape_techspodenver


def extract_exhibitors_data() -> Iterator[Dict[str, str]]:
	data = scrape_techspodenver()
	print("[INFO] Data were scraped!")

	companies = get_companies()

	for entry in data:
		if not entry['site'] or entry['company'] in companies:
			continue

		item = {
			'company': entry['company'],
			'site': entry['site'],
			'description': entry['description'],
			'decision_maker': '',
			'person_role': '',
			'person_linkedin': ''
		}

		for request, role in gen_decision_maker_request(entry['site']):
			name = ''

			# Find more info about company using ChatGPT
			if core.settings.USE_CHAT_GPT:
				response = get_chatgpt_response(request)
				print("[INFO] Request to ChatGPT was made!")

				if core.settings.USE_FREE_CHAT_GPT:
					# OpenAI allows to make not more than 3 requests per minute
					time.sleep(21)

				# Get decision-maker name
				try:
					name = extract_names(response)[0]
				except IndexError:
					name = ''
				if (name.lower() in item['company'].lower()) or len(name.split()) < 2:
					name = ''

			# Find more info about company using Google Search
			if not name:
				response = google_search(get_alternative_search_request(item['company'], role))
				if response:
					response = str(response[0]['snippet'])

				# Get decision-maker name
				try:
					name = extract_names(response)[0]
				except IndexError:
					name = ''
				if (name.lower() in item['company'].lower()) or len(name.split()) < 2:
					name = ''
				if not name:
					continue

			print("[INFO] Name was extracted!")

			# Get LinkedIn url
			item['decision_maker'], item['person_role'] = name, role
			search_request = get_linkedin_search_request(item['decision_maker'], entry['company'])
			profile_link = google_search(search_request)[0]['link']
			if 'linkedin' in profile_link and any([i.lower() in profile_link for i in name.split()]):
				item['person_linkedin'] = profile_link
			break
		yield item


if __name__ == "__main__":
	prepare_writer()
	exhibitor_extractor = extract_exhibitors_data()
	index = 1

	try:
		while True:
			exhibitor = next(exhibitor_extractor)
			write_data(exhibitor)
			print(f"[SUCCESS] №{index}: {exhibitor['company']} was successfully processed!")
			index += 1
	except StopIteration:
		...
