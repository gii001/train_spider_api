#!/usr/bin/env python
# encoding: utf-8
from constant import STATION_DICT,USER_AGENTS
import datetime
import random


def build_all_list(from_station,to_station):
    """
    构建参数列表
    :return: [[出发日期，出发车站，到达车站]] 示例：[['2019-01-20','CUW','CQW'],['2019-01-20','CUW','CXW']]
    """
    train_date = get_tomorrow()
    for i in get_dict(STATION_DICT,from_station):
        for j in get_dict(STATION_DICT,to_station):
            yield [train_date, i, j]


def get_dict(dict, value):
    """
    转化车站名,例如 将重庆返回为重庆北，重庆东
    以迭代器形式返回
    """
    for k, v in dict.items():
        if k.find(value)!= -1:
            yield v


def get_tomorrow():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    tomorrow = today + oneday
    return str(tomorrow)



def gen_headers():
    headers = {
        "User-Agent": USER_AGENTS[random.randint(0, len(USER_AGENTS) - 1)],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    return headers


def parse_train_num_json(train_json):
    """
    解析火车车次信息json，获取火车车次
    :param train_no_json: 火车车次信息json
    :return: 火车车次集合
    """
    train_num = {}
    result_re =[]
    data = train_json['data']
    result = data['result']
    for r in result:
        list_temp = r.split("|")
        if list_temp.__contains__(u"预订"):
            # 加1为爬到站时间需要的代码，加2为实际车站名字
            train_num={'train_num':list_temp[list_temp.index(u"预订") + 2],
                      'train_select_num':list_temp[list_temp.index(u"预订") + 1],
                      'start_city':list_temp[list_temp.index(u"预订") + 5],
                      'stop_city':list_temp[list_temp.index(u"预订") + 6]
                      }

        result_re.append(train_num)
    return result_re

