# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:20:35 2019

@author: cristobal.galleguill
"""
from datetime import datetime, timedelta

sec = timedelta(seconds=int(input('Enter the number of seconds: ')))
d = datetime(1,1,1) + sec
print("DAYS:HOURS:MIN:SEC")
print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))