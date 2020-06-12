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


import csv
csv_rows = []

for link in link_list:
    title = link.string
    url = link.get('href')
    csv_rows.append([title, url])

with open('./liqi_links.csv','w',newline='',encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerows(csv_rows)




