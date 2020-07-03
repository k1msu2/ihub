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
    # 조회수 랭킹
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

    # 다운로드 랭킹
    click_download = driver.find_element_by_css_selector('#popdata_css_1_2')
    click_download.click()
    download_list = driver.find_elements_by_xpath(
        '//*[@id="tabPopData2"]/ul/li[1]/a')
    d_result = []
    d_api_rank = 1
    for down in download_list:
        down_name = down.find_element_by_class_name('bbs-txt').text
        down_obj = {
            'down_name': down_name,
            'api_rank': api_rank,
        }
        d_result.append(down_obj)
        d_api_rank += 1
        print(down_name)
    context = {
        'result': result,
        'd_result': d_result,
    }
    return (request, 'rankings/index.html', context)
