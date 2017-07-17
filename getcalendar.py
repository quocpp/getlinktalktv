#!/usr/bin/python2
from lxml import html

import requests
import re
import os
import time
import json
from common import *
def getlincal(link):
    try:
        page = requests.get(link)
    except:
        dumplog("No connection")
        return ""
    if len(page.content) < 10:
        dumplog("Calendar not available")
        return ""
    resj = json.loads(page.content)
    curtime = time.localtime()
    oldtime = time.strptime(resj[0]['start_time'], '%H:%M')
    resname = resj[0]['anchor_name']
    for eresj in resj:
 #       print eresj['start_time']
        timeabc = time.strptime(eresj['start_time'], '%H:%M')
        if(timeabc.tm_hour == curtime.tm_hour):
 #           print(resname)
 #           return resname
             return eresj['anchor_name']
       # else:
       #     resname = eresj['anchor_name']
      #  print timeabc.tm_hour
    print "No thing this time"
    return ""


def GetCurrentName():
    for line in open('calendar.txt','r').readlines():
        return getlincal(line.strip())
