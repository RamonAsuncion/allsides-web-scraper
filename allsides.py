from bs4 import BeautifulSoup
import requests
from communityFeedback import *
from time import sleep
from rich.progress import track
import json


page = [
    'https://www.allsides.com/media-bias/media-bias-ratings',
]


def table(fullTable):
    # The main table
    print('Web scraper is parsing the table!')
    for url in page:
        source = requests.get(url)
        soup = BeautifulSoup(source.content, 'lxml')

        table = soup.select('tbody tr')

        for row in table:

            f = dict()  # dictionary

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
    return fullTable


def website(fullTable):
    # Enters into the info page and parses out the info
    for f in track(fullTable, description="Parsing..."):
        source = requests.get(f['News Media Info'])
        soup = BeautifulSoup(source.content, 'lxml')

        try:
            # getting the website link to news source
            website = soup.find('div', {'class': 'dynamic-grid'})
            linkToNewsSource = website.find('a')['href']
            f['News Source Site'] = linkToNewsSource
        except TypeError:
            pass
        try:
            # getting the creation date of the news source
            website = soup.find('div', {'class': 'dynamic-grid'})
            paragraph = website.find_all('p')[1].text.split('.')[-1].strip()
            f['Established'] = paragraph
        except IndexError:
            pass
        try:
            # Who the news source owned by
            website = soup.find('div', {'class': 'dynamic-grid'})
            paragraph = website.find_all('p')[2].text.split(':')[-1].strip()
            f['Owned by'] = paragraph
        except IndexError:
            pass
        sleep(10)
    return fullTable


def saving_data(fullTable):
    # Saves the data into a json file with no lines
    with open('all-sides.json', 'w', newline="") as i:
        json.dump(fullTable, i)


def main():
    # main function
    fullTable = []  # empty list
    fullTable = table(fullTable)
    fullTable = website(fullTable)
    saving_data(fullTable)

    print('Parsing has finished!')


if __name__ == '__main__':
    main()
