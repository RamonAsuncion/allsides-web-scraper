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
            f['News Media Info'] = 'https://www.allsides.com' + \
                row.select_one('.source-title a')['href']
            f['Agree'] = int(row.select_one('.agree').text)
            f['Disagree'] = int(row.select_one('.disagree').text)
            f['Ratio'] = (f['Agree'] / f['Disagree'])
            f['Community feedback'] = communityVote(f['Ratio'])
            f['Ratio'] = "{:.3f}".format(f['Ratio'])

            fullTable.append(f)  # adds it to the empty list
        sleep(10)  # this is due to the ten seconds before request in robots.txt
        print(fullTable[0])

    return fullTable


def website(fullTable):
    # Not all of them have website links
    for f in track(range(100), description="Parsing..."):
        r = requests.get(f['AllSides Bias Rating'])
        soup = BeautifulSoup(source.content, 'lxml')

        try:
            ['News Source Site']
        except TypeError:
            pass

    return fullTable
    sleep(10)


def main():
    fullTable = []  # empty list
    fullTable = table(fullTable)
    fullTable = website(fullTable)

    print('Parsing has finished!')
