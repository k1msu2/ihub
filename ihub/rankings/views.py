from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    render(request, 'rankings/index.html')
