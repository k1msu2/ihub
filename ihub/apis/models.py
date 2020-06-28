from django.db import models
from django.conf import settings

# Create your models here.
class Api(models.Model):
    # api_id = pk
    api_name = models.CharField(max_length=200)
    api_url = models.CharField(max_length=200)
    latest_modified_date = models.DateField()
    copyright = models.CharField(max_length=100)
    copyright_range = models.CharField(max_length=100)
    api_file = models.CharField(max_length=100)
    download_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='download_apis', blank=True, null=True)
    