#!/usr/bin/python2
from lxml import html
import requests
import re
import os
import time
from getcalendar import *
from common import *
import threading
import thread
from threading import Thread
threadLock = threading.Lock()
threads = []
def uploadv(link):
    threadLock.acquire()
    print("Start endcode")
    #os.system("ffmpeg -i pt2.mp4 -vcodec libx264 -preset ultrafast -af \"[0:a]atempo=1.15,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1)\" pt.mp4 -y -v 8")
    #os.system("ffmpeg -i pt2.mp4 -vcodec libx264 -preset ultrafast -af \"[0:a]atempo=1.15,volume=1.6,pan=stereo|c0<c0+0*c1|c1<c0+0*c1,aeval=val(0)|-val(1)\" pt.mp4 -y -v 8")
    os.system("cp -rfv pt2.mp4 pt.mp4")
    print("Finish endcode")
    os.system(link.encode('utf-8'))
    threadLock.release()

def getlin(link):
    try:
        page = requests.get(link)
        tree = html.fromstring(page.content)
    except:
        dumplog("No connection")
        return ""
    curname = GetCurrentName()
    
    if curname == "":
        dumplog("out time")
        return
    uploadcmd = './uploadvideo.py --file pt.mp4 --description \'Hot girl on cam\' --privacyStatus public --keywords \'talktv 69,bella,sexy dance,show hang,show cam,18+,,'+curname+'\' --title \''+curname+' on cam talktv\''
    dumplog(uploadcmd)
    for item in page.content.split(b'\n'):
        #print(item.strip())
        if b'loadPlayer.manifestUrl =' in item:
           #print(item.strip())
            match = re.findall(b"\"(.*?)\"", item.strip())
           # print(match[0])
            if ".flv" in match[0]:
#               os.system('rm -rfv ./pt.mp4')
                #os.system('cvlc -v \''+match[0]+'\' '+' --stop-time 10 --sout=file/mp4:pt.mp4 vlc://quit')
                os.system('cvlc -v \''+match[0]+'\' '+'--equalizer-preset={club} --run-time 3000  --sout=file/mp4:pt1.mp4 vlc://quit')
#                os.system(uploadcmd.encode('utf-8'))
                global threads
                if threads:
                    for t in threads:
                        t.join()
                    threads=[]
                os.system('rm -rfv ./pt2.mp4')
                os.system('rm -rfv ./pt.mp4')

                os.system("mv pt1.mp4 pt2.mp4")
                #raw_input("Press Enter to continue...")
                #thread1 = thread.start_new_thread( uploadv, (uploadcmd, ))
                thread1 = Thread(target=uploadv, args=(uploadcmd,))
                thread1.start()
                threads.append(thread1)


while (1):
    for line in open('list.txt','r').readlines():
        #print(line.strip())
        print '#',
        try:
            getlin(line.strip())
        except:
            dumplog("exception")
    time.sleep(60)
