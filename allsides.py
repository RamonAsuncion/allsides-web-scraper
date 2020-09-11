from bs4 import BeautifulSoup
import requests
from communityFeedback import *
from time import sleep
from rich.progress import track
import json


page = [
    'https://www.allsides.com/media-bias/media-bias-ratings',
]


def table(full_table):
    # The main table
    print('Web scraper is parsing the table!')
    for url in page:
        source = requests.get(url)
        soup = BeautifulSoup(source.content, 'lxml')

        main_table = soup.select('tbody tr')

        for row in main_table:

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

            full_table.append(f)  # adds it to the empty list

        sleep(10)  # this is due to the ten seconds before request in robots.txt
    return full_table


def website(full_table):
    # Enters into the info page and parses out the info
    for f in track(full_table, description="Parsing..."):
        source = requests.get(f['News Media Info'])
        soup = BeautifulSoup(source.content, 'lxml')

        try:
            # getting the website link to news source
            locate_html_class = soup.find('div', {'class': 'dynamic-grid'})
            locate_paragraph = locate_html_class.find('a')['href']
            f['News Source Site'] = locate_paragraph
        except TypeError:
            pass
        try:
            # getting the creation date of the news source
            locate__html_class = soup.find('div', {'class': 'dynamic-grid'})
            locate_paragraph = locate__html_class.find_all('p')[1].text.split('.')[-1].strip()
            f['Established'] = locate_paragraph
        except IndexError:
            pass
        try:
            # Who the news source owned by
            locate__html_class = soup.find('div', {'class': 'dynamic-grid'})
            locate_paragraph = locate__html_class.find_all('p')[2].text.split(':')[-1].strip()
            f['Owned by'] = locate_paragraph
        except IndexError:
            pass
        sleep(10)
    return full_table


def saving_data(full_table):
    # Saves the data into a json file with no lines
    with open('all-sides.json', 'w', newline="") as i:
        json.dump(full_table, i)


def main():
    # main function
    full_table = []  # empty list
    full_table = table(full_table)
    full_table = website(full_table)
    saving_data(full_table)

    print('Parsing has finished!')


if __name__ == '__main__':
    main()
