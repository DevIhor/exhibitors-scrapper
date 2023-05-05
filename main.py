import csv
import nltk
import urllib3
from bs4 import BeautifulSoup
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

try:
	nltk.data.find('tokenizers/punkt')
except LookupError:
	nltk.download('punkt')
try:
	nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
	nltk.download('averaged_perceptron_tagger')
try:
	nltk.data.find('chunkers/maxent_ne_chunker')
except LookupError:
	nltk.download('maxent_ne_chunker')
try:
	nltk.data.find('corpora/words')
except LookupError:
	nltk.download('words')


def extract_names(text):
	results = []
	nltk_results = ne_chunk(pos_tag(word_tokenize(text)))
	for nltk_result in nltk_results:
		if type(nltk_result) == Tree:
			name = ''
			for nltk_result_leaf in nltk_result.leaves():
				name += nltk_result_leaf[0] + ' '
			if nltk_result.label() == "PERSON":
				results.append(name)
	return results


def scrape_techspodenver():
	response = urllib3.request("GET", "https://techspodenver.com/exhibitors/")
	soup = BeautifulSoup(response.data, features="html.parser")
	exhibitors = soup.find("table", {"class": "exhi"}).find_all("tr")
	with open('exhibitors.csv', mode='w') as exhibitors_file:
		fieldnames = ['company', 'site', 'description']
		writer = csv.DictWriter(exhibitors_file, fieldnames=fieldnames)
		writer.writeheader()
		for item in exhibitors:
			writer.writerow({
				'company': item.find("p").find("a").text,
				'site': item.find("p").find("a")["href"],
				'description': item.find("p").text,
			})

if __name__ == "__main__":
	a = "The Academy of VR is an online learning platform that offers courses on virtual reality and related technologies. As a language model, I don't have access to current information on the specific individuals or team members who are responsible for making decisions at the Academy of VR. However, based on publicly available information, it appears that the Academy of VR was founded by Eddie Avil, who serves as the CEO of the company. Other team members listed on their website include educators, designers, and developers who contribute to creating and delivering the courses offered by the Academy of VR."
	print(extract_names(a))
	scrape_techspodenver()

