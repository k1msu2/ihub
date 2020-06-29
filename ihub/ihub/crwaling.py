import django
import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "ClienCrawlingDjango.settings")

django.setup()


def crawling_data():
    result = []
    url = 'https://data.seoul.go.kr/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    list_items = soup.find_all('div', 'bbs-list')

    for item in list_items:
        # api_name
        api_name = item.find('span', 'bbs-txt')

        item_obj = {
            'api_name': api_name,
        }
        print(api_name)
        result.append(item_obj)

    return result
