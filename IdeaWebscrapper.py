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

fullTable = soup.select('tbody tr')

# selects the first row s
row = fullTable[0]

# selects the news name of the row its targeting
newsName = row.select_one('.source-title').text.strip()

# prints out the news source name
print(newsName)

linkToNewsInfo = row.select_one('.source-title a')['href']
linkToNewsInfo = 'https://www.allsides.com' + linkToNewsInfo

# prints out the link to the news source information section
print(linkToNewsInfo)

# def saveSource(html, path):
#     with open(path, 'wb') as f:
#         f.write(html)


# saveSource()


# def readSource(html, path):
#     with open(path, 'rb') as f:
#         return f.read()


# html = readSource()
