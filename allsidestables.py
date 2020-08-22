from bs4 import BeautifulSoup
import requests
from communityFeedback import *
from time import sleep
import csv

url = 'https://www.allsides.com/media-bias/media-bias-ratings'
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')
table = soup.select('tbody tr')
row = table[0]

fullTable = []

for row in table:

    f = dict()

    f['newsName'] = row.select_one('.source-title').text.strip()
    f['linkToNewsInfo'] = 'https://www.allsides.com' + \
        row.select_one('.source-title a')['href']
    f['bias'] = row.select_one(
        '.views-field-field-bias-image a')['href'].split('/')[-1]
    f['agreeRating'] = int(row.select_one('.agree').text)
    f['disagreeRating'] = int(row.select_one('.disagree').text)
    f['ratio'] = f['agreeRating'] / f['disagreeRating']
    f['majorityCommunity'] = communityVote(f['ratio'])

    fullTable.append(f)

print(fullTable[0])

sleep(10)


# csv_file = "allsides.csv"

# with open(csv_file, 'w', newline='') as csvFile:
#     colums = ['newsName', 'linkToNewsInfo', 'bias', 'agreeRating',
#               'disagreeRating', 'ratio', 'majorityCommunity']
#     csvWriter = csv.DictReader(csvFile, fieldnames=colums)
#     csvWriter.writeheader()
#     csvWriter.writerow(f)
