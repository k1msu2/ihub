from django.shortcuts import render, get_object_or_404
import threading
from apis.models import Api 
from .models import Status
import requests
import xml.etree.ElementTree as ET
from django.http import JsonResponse

def index(request):
    apis = Api.objects.all()
    context = {
        'apis' : apis
    }
    return render(request, 'apis/index.html', context)

def detail(request, pk):
    # 추후 누적값을 저장할 코드 구현 --> Status app (DB 저장)
    api =get_object_or_404(Api,pk=pk)
    #print(api.download_users)
    context = {
        'msg' : 'success',
        'api_name' : api.api_name,
        'api_url' : api.api_url,
        'latest_modified_date' : api.latest_modified_date,
        'copyright' : api.copyright,
        'copyright_range' : api.copyright_range,
        'api_file' : api.api_file,
        'download_users' : api.download_users.all().count()
    }

    return JsonResponse(context)

# Create your views here.
def index(request):
    apis = Api.objects.all()
    context = {
        'apis' : apis
    }
    return render(request, 'apis/index.html', context)
    #response = requests.get('http://127.0.0.1:8000/articles/detail/')
    #apis = Api.objects.all()

    # 20분에 한번씩 check 하고 DB에 저장
    # for api in apis:
    #     response = requests.get(api.api_url)
    #     status_code = ET.fromstring(response.text).findtext(".//CODE")
    #     status = Status(api=api, status=status_code)
    #     status.save()

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
    # context = {
    #     'status_check': 'success',
    # }

    
    # return render(request, 'statuses/index.html', context)

def update(request, api_pk, api_status):
    api = get_object_or_404(Api, pk=api_pk)
    status = Status(api=api, status=api_status)
    status.save()
    context = {
        'status_check': 'success',
    }
    return JsonResponse(context)
