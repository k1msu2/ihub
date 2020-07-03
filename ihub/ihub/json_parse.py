import urllib.request
import json
import xmltodict
from bs4 import BeautifulSoup
import csv
from pprint import pprint
import time


def csv_parser():
    for index in range(2, 4):
        with open(f'/Users/seho/Documents/GitHub/ihub/ihub/media/api_urls_{index}_utf8.csv', newline='') as csvfile:
            urls_file = csv.reader(csvfile, delimiter=' ',  quotechar='|')
            for url in urls_file:
                # json data 생성 (json_parsing)
                key = '5161444d487365683132375755766e76'
                url = url[0].replace('(인증키)', key)
                api_eng = url.split(sep='/')[5]
                if 'xml' in url:
                    try:
                        url_new = url.replace('/5/', '/1000/')
                        xml_data = urllib.request.urlopen(
                            url_new).read().decode('utf8')
                        time.sleep(1)
                        json_data = json.dumps(xmltodict.parse(xml_data),
                                               ensure_ascii=False, indent='\t')
                        api_status = '정상'
                        with open(f'/Users/seho/Documents/GitHub/ihub/ihub/media/{api_eng}.json', 'w') as file:
                            file.write(json_data)
                    except:
                        api_status = '비정상'
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
                print(api_eng, api_status)


csv_parser()


def json_parser():
    key = '5161444d487365683132375755766e76'
    url = f'http://openapi.seoul.go.kr:8088/{key}/xml/pmisSafetyCheckD/1/1/043012061101/20160211'
    api_eng = url.split(sep='/')[5]

    xml_data = urllib.request.urlopen(url).read().decode('utf8')

    # json 변환을 위해 변수에 ensure_ascii=False 값 주기, indent='t' 띄어쓰기
    json_data = json.dumps(xmltodict.parse(xml_data),
                           ensure_ascii=False, indent='\t')
    # print(json_data)
    with open(f'/Users/seho/Documents/GitHub/ihub/ihub/media/{api_eng}.json', 'w') as file:
        file.write(json_data)


# json_parser()
