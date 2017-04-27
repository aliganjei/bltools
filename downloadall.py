#!/usr/bin/env python3.5
import os,random,sys,time,subprocess

SLEEPTIME = 300
TARGETDIR = '/Users/Ali/royal'
RANGEBEGIN = 100
RANGEEND = 150
COMMAND = 'dezoomify-node.js'
CWD = '/Users/Ali/workspace/dezoomify/master/node-app/'
URL = "http://www.bl.uk/manuscripts/Proxy.ashx?view=io_islamic_3541_{}.xml"
SAVETO = "{}/{}"


def trydownload(filename):
   url = URL.format(filename.split('.')[0])
   saveto = SAVETO.format(TARGETDIR,filename)
   print(COMMAND)
   subprocess.run(['node',COMMAND,url,saveto],cwd=CWD)
   return


def updatedownloaded(d,c):
   #if random.randint(1,5) <= 3:
   if c in os.listdir(TARGETDIR):
      d.append(c)
      print('{} downloaded successfully'.format(c))
   return

missingfiles = []

rs = ['f{:03d}r.jpg'.format(x) for x in range(RANGEBEGIN,RANGEEND)]
vs = ['f{:03d}v.jpg'.format(x) for x in range(RANGEBEGIN,RANGEEND)]

allfiles = rs + vs
downloaded = os.listdir(TARGETDIR)

missingfiles = list(set(allfiles).difference(set(downloaded)))

print(missingfiles)

while missingfiles:
   candidate = random.sample(missingfiles,1)[0]
   trydownload(candidate)
   print('Sleeping ...')
   for i in range(SLEEPTIME//5):
       print('.',end='',flush=True)
       time.sleep(5)
   updatedownloaded(downloaded,candidate)
   if candidate in downloaded:
       missingfiles.remove(candidate)

