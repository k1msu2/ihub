from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'http://data.seoul.go.kr/'


def crawling():
    driver = webdriver.Chrome(ChromeDriverManager().install())
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


# crawling()
