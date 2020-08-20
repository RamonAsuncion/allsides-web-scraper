from communityFeedback import *
from bs4 import BeautifulSoup
import requests

# imports the functions from the py file to this one

# url of the website url
url = 'https://www.allsides.com/media-bias/media-bias-ratings'

# get the source code
source = requests.get(url)

#
soup = BeautifulSoup(source.content, 'lxml')

# first 50 characters of the source code to test
# print(source.content[:50])

# Contains News source name, community feedback, link to news source, and bias data.
table = soup.select('tbody tr')

# selects the first row
row = table[0]

# selects the news name of the row its targeting
newsName = row.select_one('.source-title').text.strip()

# prints out the news source name
# print(newsName)

linkToNewsInfo = row.select_one('.source-title a')['href']

linkToNewsInfo = 'https://www.allsides.com' + linkToNewsInfo

# prints out the link to the news source information section
# print(linkToNewsInfo)

biasCheck = row.select_one('.views-field-field-bias-image a')['href']

# splits whats to the left of the /
biasCheck = biasCheck.split('/')[-1]

# prints out if the source is left, left-center, right, right center, center...
# print(biasCheck)

# selects the value for how many agree that their political side is correct
agreeRating = row.select_one('.agree').text

# turns the string to an integer
agreeRating = int(agreeRating)

# selects the value for how many disagree that their political side is correct
disagreeRating = row.select_one('.disagree').text

# turns the string to an integer
disagreeRating = int(disagreeRating)

# finds the ratio by dividing both of them by eachother
ratio = agreeRating / disagreeRating

# prints out the rating in print f format
# print(
#     f'Agree: {agreeRating:} Disagree: {disagreeRating:} Ratio (Agree/Disagree): {ratio:.3f}')

# the "somewhat agrees string" was rendered with javascript
# print("Majority of the community: " + communityVote(ratio))

table = []

for row in table:

    d = dict()

    d['newsName'] = row.select_one('.source-title').text.strip()
    d['linkToNewsInfo'] = row.select_one('.source-title a')['href']
    d['linkToNewsInfo'] = 'https://www.allsides.com' + linkToNewsInfo
    d['biasCheck'] = row.select_one('.views-field-field-bias-image a')['href']
    d['biasCheck'] = biasCheck.split('/')[-1]
    d['agreeRating'] = row.select_one('.agree').text
    d['agreeRating'] = int(agreeRating)
    d['disagreeRating'] = row.select_one('.disagree').text
    d['disagreeRating'] = int(disagreeRating)
    d['ratio'] = agreeRating / disagreeRating

    table.append(d)
    print(fullTable[0])
