from bs4 import BeautifulSoup
import requests
from communityFeedback import *
from time import sleep
import csv

fullTable = []

pages = {
    'https://www.allsides.com/media-bias/media-bias-ratings'
}

for url in pages:

    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')
    table = soup.select('tbody tr')
    row = table[0]


    for row in table:

        f = dict()

        f['newsName'] = row.select_one('.source-title').text.strip()
        f['linkToNewsInfo'] = 'https://www.allsides.com' + \
            row.select_one('.source-title a')['href']
        f['bias'] = row.select_one(
            '.views-field-field-bias-image a')['href'].split('/')[-1]
        f['agree'] = int(row.select_one('.agree').text)
        f['disagree'] = int(row.select_one('.disagree').text)
        f['ratio'] = f['agree'] / f['disagree']
        f['majorityCommunity'] = communityVote(f['ratio'])

        fullTable.append(f)

print(fullTable[1])

sleep(10) # this is due to the ten seconds before request in robots.txt



