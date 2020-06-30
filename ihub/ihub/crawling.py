from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'http://data.seoul.go.kr/'


def crawling():
    driver = webdriver.Chrome(
        ChromeDriverManager().install())
    driver.get(url)
    time.sleep(2)
    api_list = driver.find_elements_by_xpath(
        '//*[@id="tabPopData1"]/ul/li/a')
    result = []
    api_rank = 1
    for api in api_list:
        api_name = api.text
        api_url = api.get_attribute('href')
        api_obj = {
            'api_name': api_name,
            'api_url': api_url,
            'api_rank': api_rank,
        }
        result.append(api_obj)
        api_rank += 1


def crawling_api_inform():
    # datasetVO > div.wrap-a > div > section > div.list-statistics > dl:nth-child(1)
    # datasetVO > div.wrap-a > div > section > div.list-statistics > dl:nth-child(2)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=options)
    driver.get(url)
    time.sleep(1)
    click_api = driver.find_elements_by_css_selector(
        '#datasetVO > div.wrap-a > div > section > div.list-statistics > dl:nth-child(1) > dt > a')
    print(click_api)


crawling_api_inform()
