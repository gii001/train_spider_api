#!/usr/bin/env python
# encoding: utf-8

from constant import STATION_DICT,USER_AGENTS
import datetime
import random


def get_tomorrow():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    tomorrow = today + oneday
    return str(tomorrow)





def __gen_headers():
    headers = {
        "User-Agent": USER_AGENTS[random.randint(0, len(USER_AGENTS) - 1)],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    return headers