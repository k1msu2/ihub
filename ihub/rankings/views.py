from django.shortcuts import render, redirect
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint
import time

url = 'http://data.seoul.go.kr/'


def index(request):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=options)
    driver.get(url)
    time.sleep(1)
    api_list = driver.find_elements_by_xpath(
        '//*[@id="tabPopData1"]/ul/li/a')
    result = []
    api_rank = 1
    for api in api_list:
        # print(dir(api))
        api_name = api.find_element_by_class_name('bbs-txt').text
        pprint(api_name)
        api_url = api.get_attribute('href')
        api_obj = {
            'api_name': api_name,
            'api_url': api_url,
            'api_rank': api_rank,
        }
        result.append(api_obj)
        api_rank += 1
    # print(result[0].get('api_name'))
    context = {
        'result': result,
    }
    return render(request, 'rankings/index.html', context)
