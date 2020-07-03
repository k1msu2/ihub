from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from pprint import pprint
import urllib.request
import json
import xmltodict
from bs4 import BeautifulSoup


url = 'http://data.seoul.go.kr/'


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

    for i in range(4, 13):
        for index in range(apis_len):
            api = driver.find_elements_by_css_selector(
                '#datasetVO > div.wrap-a > div > section > div.list-statistics > dl > dt > a > strong')[index]
            api_name = api.text
            api.click()
            time.sleep(3)
            # OPEN API 클릭하기
            # uiTabguide1 > div.ui-tab-btns.col6 > button:nth-child(2)
            selection = len(driver.find_elements_by_css_selector(
                '#uiTabguide1 > div.ui-tab-btns.col6 > button'))
            if selection >= 2:
                select_api = driver.find_element_by_css_selector(
                    '#uiTabguide1 > div.ui-tab-btns.col6 > button:nth-child(2)')
                select_api.click()
                time.sleep(3)

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

            # json data 생성 (json_parsing)
            key = '5161444d487365683132375755766e76'
            url = api_url.replace('(인증키)', key)
            if url.split(sep='/')[4] == 'xml':
                try:
                    url_new = url.replace('/5/', '/1000/')
                    xml_data = urllib.request.urlopen(
                        url_new).read().decode('utf8')
                    time.sleep(1)
                    json_data = json.dumps(xmltodict.parse(xml_data),
                                           ensure_ascii=False, indent='\t')
                    api_status = '정상'
                except:
                    api_status = '비정상'
                with open(f'/Users/seho/Documents/GitHub/ihub/ihub/media/{api_eng}.json', 'w') as file:
                    file.write(json_data)
            else:
                try:
                    json_data = urllib.request.urlopen(
                        url).read().decode('utf8')
                    json_data_new = json.loads(json_data)
                    total = json_data_new[api_eng]["list_total_count"]
                    url_new = url.replace('/5/', f'/{total}/')
                    json_data = urllib.request.urlopen(
                        url_new).read().decode('utf8')
                    api_status = '정상'
                    with open(f'/Users/seho/Documents/GitHub/ihub/ihub/media/{api_eng}.json', 'w') as file:
                        file.write(json_data)
                except:
                    api_status = '비정상'

            api_inform = {
                'api_name': api_name,
                'api_url': url,
                'latest_modified_date': latest_modified_date,
                'copyright': copyright,
                'copyright_range': copyright_range,
                'api_file': api_file,
                'api_status': api_status,
            }
            pprint(api_inform)
            driver.execute_script("window.history.go(-1)")
            time.sleep(1)
            if index == 10:
                break
        # 페이지 넘기기
        time.sleep(1)
        if i <= 12:
            next_page = driver.find_element_by_css_selector(
                f'#datasetVO > div.wrap-a > div > section > div.list-statistics > div > div > button:nth-child({i})')
            next_page.click()
        else:
            next_page = driver.find_element_by_css_selector(
                '#datasetVO > div.wrap-a > div > section > div.list-statistics > div > div > button.paging-next')
            next_page.click()


# crawling_api_inform()

def down_ranking():
    driver = webdriver.Chrome(
        ChromeDriverManager().install())
    driver.get(url)
    time.sleep(1)

    # 다운로드 랭킹
    click_download = driver.find_element_by_css_selector('#popdata_css_1_2')
    click_download.click()
    download_list = driver.find_elements_by_xpath(
        '//*[@id="tabPopData2"]/ul/li/a')
    d_result = []
    api_rank = 1
    for down in download_list:
        down_name = down.find_element_by_class_name('bbs-txt').text
        down_obj = {
            'down_name': down_name,
            'api_rank': api_rank,
        }
        d_result.append(down_obj)
        api_rank += 1
        print(down_name)


down_ranking()
