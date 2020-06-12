import csv
import requests
from bs4 import BeautifulSoup

import csv
data = open('./liqi_links.csv')

reader = csv.reader(data)

rows = [row for row in reader]


count = 0
for row in rows:
    title = row[0]
    url = row[1]
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    with open("./static/{}.html".format(title), "w") as file:
        file.write(str(soup))

    print('now: ' + str(count))
    count += 1
