#!/usr/bin/python2
from lxml import html
import requests
import re
import os
import time

def getweeklist(link):
    gdata = getlin(link)
    fstrre = "<span data-reactid=\"[0-9]+\">Week [0-9]</span>"
    linkre = "\"nav_week\" data-track-href=\"/learn.*?\""
    print fstrre
    matchswname = re.findall(fstrre,gdata)
    for match in matchswname:
        print match

    matchslink = re.findall(linkre,gdata)
    for match1 in matchslink:
        print match1


def getlin(link):
    #try:
        cookiess={'CAUTH':'KjifOb4U7RNIvpTKJ2PnouIGseqYTtCUvKFQ063YvGcKgbTRq7qixohbrRijFrNhEUPzO5ggThOY0f6eNhRaTg.QFvZ9c1IUDOxxPC3bu6K4w.O9-XBp6hyn2IoBDY_7GBLUOiMzA9SKASgy_KXcs6YxMW_b5_2ynVNVni6UuetH2iogoMTjQMFLm0g7qKGNrr7-dEl9Mhk39tkol49mWDJWj_Wqyk3--icY7muGXkFgvLGf39iCzJnsqvY9r3-5mj1K6V5YNyEOC6CL9js6PCB1kk4haGr9CpSRCTndCywQi8',
                'CSRF3-Token':'1494729649.WzBGvcOr1svbRSBI'
                      }
        page = requests.get(link,cookies=cookiess)
        return page.content
        #print page.content
    #except:
        
#while (1):
for line in open('list.txt','r').readlines():
    print(line.strip())
    print '#',
    getweeklist(line.strip())
