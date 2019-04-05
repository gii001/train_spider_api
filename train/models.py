from django.db import models

# Create your models here.
class Basic_info(models.Model):
    EasyName=models.CharField(max_length='20')
    RealName=models.CharField(max_length='20')
    StartStation=models.CharField(max_length='10')
    StopSttation=models.CharField(max_length='10')
class Station(models.Model):
    NowNum=models.IntegerField(max_length='10')
    NowStation=models.CharField(max_length='10')
    EasyName = models.ForeignKey('Basic_info', on_delete=models.CASCADE)