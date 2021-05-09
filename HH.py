import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

def get(url, params, headers):
    req = requests.get(url, params=params, headers=headers)
    return req


url = "https://spb.hh.ru/search/vacancy/"
params = {"clusters": "true",
          "area": "2",
          "enable_snippets": "true",
          "salary": "",
          "st": "searchVacancy",
          "text": "Архивариус",
          "from": "suggest_post",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

r = get(url, params, headers)

soup = bs(r.text, "html.parser")
ihh = soup.find_all("div", class_="vacancy-serp-item__row vacancy-serp-item__row_header")
links = soup.find_all("a", class_="bloko-link")

final_link = []
for link in links:
    link_url = link.get("href")
    if "https://spb.hh.ru/vacancy" in link_url:
        final_link.append(link_url)

k = []
for x in ihh:
    u = x.text
    u = u.replace("\u202f", "").split()
    k.append(u)

final_cut = []
i = 0
for i in range(0, len(final_link)):
    final_cut.append([k[i], final_link[i]])
    i = i + 1

pprint(final_cut)