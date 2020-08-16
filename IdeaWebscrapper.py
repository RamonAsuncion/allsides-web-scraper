from bs4 import BeautifulSoup
import requests

url = 'https://www.allsides.com/media-bias/media-bias-ratings'

source = requests.get(url)

soup = BeautifulSoup(source.content, 'lxml')


print(source.content[:50])  # first 50 characters of the source code to test

rows = soup.select('tbody tr')

row = rows[0]


linkToNewsInfo = row.select_one('.source-title a')['href']
linkToNewsInfo = 'https://www.allsides.com' + linkToNewsInfo

print(websitePage)

# def saveSource(html, path):
#     with open(path, 'wb') as f:
#         f.write(html)


# saveSource()


# def readSource(html, path):
#     with open(path, 'rb') as f:
#         return f.read()


# html = readSource()
