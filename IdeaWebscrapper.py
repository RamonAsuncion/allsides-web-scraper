from bs4 import BeautifulSoup
import requests

source = requests.get('https://ramonasuncion.me/')


def saveSource(html, path):
    with open(path, 'wb') as f:
        f.write(html)


saveSource(r.content, 'ramonasuncion_me')
