from django.shortcuts import render
import threading
from apis.models import Api 
from .models import Status
import requests
import xml.etree.ElementTree as ET

# Create your views here.
def index(request):
    #response = requests.get('http://127.0.0.1:8000/articles/detail/')
    apis = Api.objects.all()

    # 20분에 한번씩 check 하고 DB에 저장
    for api in apis:
        response = requests.get(api.api_url)
        status_code = ET.fromstring(response.text).findtext(".//CODE")
        status = Status(api=api, status=status_code)
        status.save()

    #response = requests.get('http://openapi.seoul.go.kr:8088/7a414542756b316d3132377954467477/xml/MonthlyAverageAirQuality/1/5/201212')
    # print(response.text)
    # xml_root = ET.fromstring(response.text)
    #print(xml_root)
    # print((response.json())['MonthlyAverageAirQuality']['RESULT']['CODE'])
    # CODE = (response.json())['MonthlyAverageAirQuality']['RESULT']['CODE']
    # print(response.status_code)
    #for child in xml_root:
    #    print(child.tag, child.attrib)
    
    # print(xml_root.find('RESULT/CODE').text)
    #print(xml_root[0].text)
    context = {
        'status_check': 'success',
    }

    
    return render(request, 'statuses/index.html', context)
