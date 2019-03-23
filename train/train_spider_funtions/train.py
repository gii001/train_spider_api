#!/usr/bin/env python
# encoding: utf-8


import requests

from constant import *

from funtions import *

def get_train(arg):
     train_no_url = TRAIN_NO_BASE_URL + 'leftTicketDTO.train_date=' + str(arg[0]) + '&leftTicketDTO.from_station=' + str(arg[1]) + '&leftTicketDTO.to_station=' + str(arg[2]) + PURPOSE_CODES
     response = requests.get(train_no_url,headers=gen_headers())
     train_json = response.json()
     return parse_train_num_json(train_json)
def get_station(arg,train_num):
     station_info_url = STATION_INFO_BASE_URL + 'train_no=' + train_num + '&from_station_telecode=' + str(arg[1]) + '&to_station_telecode=' + str(arg[2]) + '&depart_date=' + str(arg[0])
     response = requests.get(station_info_url,headers=gen_headers())
     train_json = response.json()
     return train_json
def get_train_start(from_station,to_station):
    result = []
    for i in build_all_list(from_station,to_station):
        result.append(get_train(i))
    return result


def get_station_start(from_station,to_station,train_num):
        i=[get_tomorrow(),from_station,to_station]
        return get_station(i,train_num)

if __name__ == '__main__':
    for i in build_all_list('西安','杭州'):

            for k,v in get_train(i).items():
                get_station(i,v)