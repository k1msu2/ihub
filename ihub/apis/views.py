from django.shortcuts import render, redirect, get_object_or_404
from .models import Api
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from django.core import serializers
from statuses.models import Status
import os
from django.conf import settings
from django.http import HttpResponse, Http404
# Create your views here.
from django.contrib.auth.decorators import login_required
import urllib.request
import mimetypes

def index(request):
    apis = Api.objects.all()
    context = {
        'apis' : apis
    }
    return render(request, 'apis/index.html', context)

def detail(request, pk):
    # 추후 누적값을 저장할 코드 구현 --> Status app (DB 저장)
    api = get_object_or_404(Api,pk=pk)
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

def search(request, search_string):
    api = get_object_or_404(Api, api_name=search_string)
    context = {
        'msg' : 'success',
        'api_pk' : api.pk
    }
    return JsonResponse(context) 

def status(request, pk):
    #status = get_object_or_404(Status, api_id=pk)
    latest_status = Status.objects.filter(api_id=pk).latest('updated_time')
    print(latest_status.updated_time)
    context = {
        'msg' : 'success',
        'latest_status' : latest_status.status
    }
    return JsonResponse(context) 

def download(request, pk):
    api = get_object_or_404(Api, pk=pk)
    file_path = os.path.join(settings.MEDIA_ROOT, api.api_file)
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_path)[0])
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404