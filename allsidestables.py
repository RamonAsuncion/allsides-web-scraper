from bs4 import BeautifulSoup
import requests
from communityFeedback import *
from time import sleep
import csv

fullTable = []  # empty list


pages = [
    'https://www.allsides.com/media-bias/media-bias-ratings',
    # found in source code line #2787 for ?page=1
    'https://www.allsides.com/media-bias/media-bias-ratings?page=1',
]

for url in pages:

    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')
    table = soup.select('tbody tr')

    for row in table:

        f = dict()

        f['News Source'] = row.select_one('.source-title').text.strip()
        f['AllSides Bias Rating'] = row.select_one(
            '.views-field-field-bias-image a')['href'].split('/')[-1]
        f['linkToNewsInfo'] = 'https://www.allsides.com' + \
            row.select_one('.source-title a')['href']
        f['agree'] = int(row.select_one('.agree').text)
        f['disagree'] = int(row.select_one('.disagree').text)
        f['ratio'] = (f['agree'] / f['disagree'])
        f['Community feedback'] = communityVote(f['ratio'])

        fullTable.append(f)  # adds it to the empty list

print(fullTable[30])  # prints out the specific row

sleep(10)  # this is due to the ten seconds before request in robots.txt
print("10 seconds have passed")
