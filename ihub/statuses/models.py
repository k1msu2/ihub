from django.db import models
from apis.models import Api

# Create your models here.
class Status(models.Model):
    api = models.ForeignKey(Api, on_delete=models.CASCADE)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100)
    class Meta:
        ordering = ['-id']
    
