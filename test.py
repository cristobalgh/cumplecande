# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:26:23 2019

@author: cristobal.galleguill
"""

import datetime

now = datetime.datetime.now()
si_cumple = now.month==12 and now.day==27

today = now
my_birthday = datetime.datetime(today.year, 12, 27, 0, 0, 0)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
dt = my_birthday - today
print(dt.total_seconds())