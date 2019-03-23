#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
import json,sys
from train.train_spider_funtions.train import *
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

# Create your views here.




def train(response,from_station,to_station):
    result = get_train_start(from_station,to_station)
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


def station(response,from_station,to_station,train_name):
    result = get_station_start(from_station,to_station,train_name)
    a=1
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")