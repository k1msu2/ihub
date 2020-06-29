from django.shortcuts import render, redirect, get_object_or_404
from .models import Api
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from django.core import serializers
# Create your views here.
from django.contrib.auth.decorators import login_required

def index(request):
    apis = Api.objects.all()
    context = {
        'apis' : apis
    }
    return render(request, 'apis/index.html', context)

def detail(request, pk):
    # 추후 누적값을 저장할 코드 구현 할것 
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