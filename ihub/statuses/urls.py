from django.urls import path
from . import views

app_name = 'statuses'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:api_pk>/<api_status>', views.update, name='update')
]
