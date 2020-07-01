import urllib.request
import json
import xmltodict
from bs4 import BeautifulSoup


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
