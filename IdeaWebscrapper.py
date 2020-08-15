from bs4 import BeautifulSoup
import requests

url = 'https://ramonasuncion.me/'

source = requests.get(url)


def saveSource(html, path):
    with open(path, 'wb') as f:
        f.write(html)


saveSource(r.content, 'ramonasuncion_me')


def readSource(html, path):
    with open(path, 'rb') as f:
        return f.read()


html = readSource('ramonasuncion_me')
