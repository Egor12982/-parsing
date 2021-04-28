import requests
from pprint import pprint
import json

url = "https://api.github.com/users/Egor12982/repos"
r = requests.get(url)

print(url)
data = r.json()
pprint(data)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)
