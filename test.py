from bs4 import BeautifulSoup
import requests
from time import sleep


url = "https://www.allsides.com/media-bias/media-bias-ratings"
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')

table = soup.select('tbody tr')

website = soup.select_one('.fa')['href']
print(website)

sleep(10)
print("continue on testing 10 seconds have passed")
