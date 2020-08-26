from bs4 import BeautifulSoup
import requests
from communityFeedback import *
from time import sleep
from rich.progress import track

pages = [
    'https://www.allsides.com/media-bias/media-bias-ratings',
    # found in html source code line #2787 for ?page=1
    'https://www.allsides.com/media-bias/media-bias-ratings?page=1',
]


def table(fullTable):
    print("table")

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
            f['ratio'] = "{:.3f}".format(f['ratio'])

            fullTable.append(f)  # adds it to the empty list
        sleep(10)  # this is due to the ten seconds before request in robots.txt
        print(fullTable[0])

    return fullTable


def website(fullTable):
    # Not all of them have website links
    for d in track(range(100), description="Parsing..."):
        r = requests.get(f['AllSides Bias Rating'])
        soup = BeautifulSoup(source.content, 'lxml')

        try:
            ['News Source Site']
        except TypeError:
            pass

    return fullTable


def main():
    fullTable = []  # empty list
    fullTable = table(fullTable)
    fullTable = website(fullTable)

    print('Parsing has finished!')
