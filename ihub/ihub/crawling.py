from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from pprint import pprint


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
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1920x1080')
    # options.add_argument("disable-gpu")
    driver = webdriver.Chrome(
        ChromeDriverManager().install())  # , chrome_options=options)
    url = 'http://data.seoul.go.kr/dataList/datasetList.do'
    driver.get(url)
    time.sleep(1)
    # api 만 있는 페이지로 이동
    click_api_only = driver.find_element_by_css_selector(
        '#serviceGroups > li:nth-child(2) > button')
    click_api_only.click()

    # api 들어가기
    apis_len = len(driver.find_elements_by_css_selector(
        '#datasetVO > div.wrap-a > div > section > div.list-statistics > dl > dt > a > strong'))

    # pprint(apis)
    for i in range(4, 13):
        for index in range(apis_len):
            api = driver.find_elements_by_css_selector(
                '#datasetVO > div.wrap-a > div > section > div.list-statistics > dl > dt > a > strong')[index]
            api_name = api.text
            api.click()
            time.sleep(3)
            # 크롤링 다시 시작할때 여기부터 하기!!!!!!!!!!!
            api_url = driver.find_element_by_css_selector(
                '#frm2 > div:nth-child(5) > table > tbody > tr:nth-child(1) > td > a').text
            latest_modified_date = driver.find_element_by_css_selector(
                '#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(1) > td:nth-child(4) > span').text
            copyright = driver.find_element_by_css_selector(
                '#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(3) > td:nth-child(4)').text
            copyright_range = driver.find_element_by_css_selector(
                '#frm > div:nth-child(10) > div.tbl-base-d.align-l.only-d2 > table > tbody > tr:nth-child(7) > td > div').text
            api_eng = api_url.split(sep='/')[5]
            api_file = f'{api_eng}.json'
            # pprint(api_name)
            pprint(api_file)
            # pprint(latest_modified_date)
            # pprint(copyright)
            # pprint(copyright_range)
            driver.execute_script("window.history.go(-1)")
            time.sleep(1)
            if index == 10:
                break
        time.sleep(3)
        if i <= 12:
            next_page = driver.find_element_by_css_selector(
                f'# datasetVO > div.wrap-a > div > section > div.list-statistics > div > div > button:nth-child({i})')
        else:
            next_page = driver.find_element_by_css_selector(
                f'# datasetVO > div.wrap-a > div > section > div.list-statistics > div > div > button.paging-next')
        next_page.click()


def test():
    driver = webdriver.Chrome(
        ChromeDriverManager().install())  # , chrome_options=options)
    url = 'http://data.seoul.go.kr/dataList/datasetList.do'
    driver.get(url)
    time.sleep(3)
    # api 만 있는 페이지로 이동
    click_api_only = driver.find_element_by_css_selector(
        '#serviceGroups > li:nth-child(2) > button')
    click_api_only.click()
    for i in range(4, 13):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        if i <= 12:
            next_page = driver.find_elements_by_css_selector(
                f'# datasetVO > div.wrap-a > div > section > div.list-statistics > div > div > button:nth-child({i})')
        else:
            next_page = driver.find_element_by_css_selector(
                f'# datasetVO > div.wrap-a > div > section > div.list-statistics > div > div > button.paging-next')
        next_page.click()


# crawling_api_inform()
test()
