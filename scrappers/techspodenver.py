from typing import List, Dict

import urllib3
from bs4 import BeautifulSoup


def scrape() -> List[Dict[str, str]]:
    """
    Scrapes exhibitors data from techspodenver.com
    """
    results = []
    response = urllib3.request("GET", "https://techspodenver.com/exhibitors/")
    soup = BeautifulSoup(response.data, features="html.parser")
    exhibitors = soup.find("table", {"class": "exhi"}).find_all("tr")
    for item in exhibitors:
        results.append({
            'company': item.find("p").find("a").text,
            'site': item.find("p").find("a")["href"],
            'description': item.find("p").text,
        })
    return results
