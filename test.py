from bs4 import BeautifulSoup
import requests
from time import sleep


url = "https://www.allsides.com/media-bias/media-bias-ratings"
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')

table = soup.select('tbody tr')


website = soup.select_one('a')['href']

fullTable = []  # empty list

for row in table:
    f = dict()
    f['AllSides Bias Rating'] = row.select_one(
        '.views-field-field-bias-image a')['href'].split('/')[-1]

    fullTable.append(f)

print(fullTable[0])


sleep(10)
print("continue on testing 10 seconds have passed")
