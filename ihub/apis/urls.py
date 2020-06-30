from django.urls import path
from . import views

app_name = 'apis'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('search/<search_string>/', views.search, name='search'),
    path('status/<int:pk>/', views.status, name='status')
]
