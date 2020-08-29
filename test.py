from bs4 import BeautifulSoup
import requests
from communityFeedback import *
from time import sleep
from rich.progress import track
import csv


url = "https://www.allsides.com/news-source/abc-news-media-bias"
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')

pages = [
    'https://www.allsides.com/media-bias/media-bias-ratings',
    # found in html source code line #2787 for ?page=1
    'https://www.allsides.com/media-bias/media-bias-ratings?page=1',
]

website = soup.find('div', {'class': 'dynamic-grid'})
link = website.find_all('p')[1].text.split('.')[-1].strip()


table = soup.select('tbody tr')

fullTable = []  # empty list

for url in pages:
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')

    table = soup.select('tbody tr')

    for row in table:

        f = dict()

        f['News Media Info'] = 'https://www.allsides.com' + \
            row.select_one('.source-title a')['href']

        fullTable.append(f)  # adds it to the empty list

    sleep(10)  # this is due to the ten seconds before request in robots.txt

for i in track(range(100), description="Parsing..."):
    source = requests.get(f['News Media Info'])
    soup = BeautifulSoup(source.content, 'lxml')

    try:
        # getting the website link to news source
        website = soup.find('div', {'class': 'dynamic-grid'})
        link = website.find('a')['href']
        f['News Source Site'] = link
    except TypeError:
        pass

    try:
        # getting the creation date of the news source
        website = soup.find('div', {'class': 'dynamic-grid'})
        paragraphTag = website.find_all('p')[1].text.split('.')[-1].strip()
        f['Established:'] = paragraphTag
    except TypeError:
        pass
