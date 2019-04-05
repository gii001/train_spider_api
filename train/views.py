#!/usr/bin/env python
# encoding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from models import *
import json,sys
from train.train_spider_funtions.train import *
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

# Create your views here.




def train(response,from_station,to_station):
    result = get_train_start(from_station,to_station)
    for i in result[0]:
        if Basic_info.objects.filter(RealName=i['train_select_num']):
            continue

        else:
            b=Basic_info()
            b.EasyName = i["train_select_num"]
            b.RealName = i['train_num']
            b.StartStation = i['start_city']
            b.StopStation = i['stop_city']
            b.save()






    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


def station(response,from_station,to_station,train_name):
    result = get_station_start(from_station,to_station,train_name)
    for i in result['data']['data']:
        if Station.objects.filter(NowNum = i['station_no']):
            continue
        else:
            s = Station()
            s.NowNum = i['station_no']
            s.NowStation = i['station_name']
            s.EasyName = Basic_info.objects.filter(RealName='train_name')
            s.save()

    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")