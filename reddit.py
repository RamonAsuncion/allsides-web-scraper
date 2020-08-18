from bs4 import BeautifulSoup
import requests

# url to the website url
url = 'https://www.allsides.com/media-bias/media-bias-ratings'

# get the source code
source = requests.get(url)

#
soup = BeautifulSoup(source.content, 'lxml')

# first 50 characters of the source code to test
print(source.content[:50])

# Contains News source name, community feedback, link to news source, and bias data.
fullTable = soup.select('tbody tr')

# selects the first row
row = fullTable[0]

# selects the news name of the row its targeting
newsName = row.select_one('.source-title').text.strip()

# prints out the news source name
print(newsName)

linkToNewsInfo = row.select_one('.source-title a')['href']

linkToNewsInfo = 'https://www.allsides.com' + linkToNewsInfo

# prints out the link to the news source information section
print(linkToNewsInfo)

biasCheck = row.select_one('.views-field-field-bias-image a')['href']

# splits whats to the left of the /
biasCheck = biasCheck.split('/')[-1]

# prints out if the source is left, left-center, right, right center, center...
print(biasCheck)