import urllib.parse
import requests
from bs4 import BeautifulSoup


r = requests.get('https://liqi.io/creators/')

soup = BeautifulSoup(r.text)
raw_link_list = soup.find_all('a')[33:-7]

link_list = []
for raw_link in raw_link_list:
    if "月" in str(raw_link) and "201" in str(raw_link):
        continue
    link_list.append(raw_link)

for i in link_list:
    i['href'] = "./static/" + urllib.parse.quote(i.string) + '.html'




with open("./liqi_index.html".format(title), "w") as file:
    file.write(str(soup))