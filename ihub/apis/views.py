from django.shortcuts import render
from accounts.models import Api
# Create your views here.


def index(request):
    apis = Api.objects.all()
    context = {
        'apis': apis
    }
    return render(request, 'apis/index.html', context)
