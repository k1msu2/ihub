from django.urls import path
from . import views

app_name = 'statuses'
urlpatterns = [
    path('', views.index, name='index'),
]
