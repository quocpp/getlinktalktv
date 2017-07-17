#!/usr/bin/python2
from time import gmtime, strftime, localtime
def dumplog(logerr):
    print strftime("%Y-%m-%d %H:%M:%S", localtime())+" "+logerr
