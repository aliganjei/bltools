#!/usr/bin/env python3.6
import os,random,sys,time,requests
from PIL import Image
from io import BytesIO
import xmltodict
import yaml

def readconfig():
    return yaml.safe_load(open("bl.conf"))


def getfileinfo(filename):
   infourl = BASEURL + MANUSCRIPTID + '_' + filename.split('.')[0] + '.xml'
   response = s.get(infourl)
   infodict = xmltodict.parse(BytesIO(response.content))
   w = int(infodict['Image']['Size']['@Width']) -1
   h = int(infodict['Image']['Size']['@Height']) -1
   t = int(infodict['Image']['@TileSize'])
   print (w,h,t)
   return (w,h,t)

def trydownload(filename):
   print('Downloading ',filename)
   (width,height,tilesize) = getfileinfo(filename)
   rows = (width // tilesize) + 1
   cols = (height // tilesize) + 1
   zoomlevel = 13
   tileurl = BASEURL + MANUSCRIPTID + '_' + filename.split('.')[0] + '_files/' + str(zoomlevel) + '/{}_{}.jpg'
   alltilesurls = [tileurl.format(x,y) for x in range(rows) for y in range(cols)]
   x = 0
   y = 0
   page = Image.new("RGB",(width,height))
   tiles = []
   fuckedup = False
   partial = ''
   for f in alltilesurls:
      response = s.get(f)
      try:
         tile = Image.open(BytesIO(response.content))
      except:
         tile = Image.new("RGB",(tilesize,tilesize))
         fuckedup = True
         print('*',end='',flush=True)
      tiles.append(tile)
      print('.',end='',flush=True)
   print('')
   if fuckedup:
       print('****** Some tiles didnt load properly  *****')
       partial = 'partial-'

   for t in tiles:
      box = (x*tilesize, y*tilesize)
      y += 1
      if y == cols:
          y = 0
          x += 1
      page.paste(t,box)
   page.save(TARGETDIR+'/{}{}'.format(partial,filename))

def updatedownloaded(d,c):
   if c in os.listdir(TARGETDIR):
      d.append(c)
   return

config = readconfig()
BASEDIR = config["basedir"]
SLEEPTIME = config["sleeptime"]
RANGEBEGIN = config["rangebegin"]
RANGEEND = config["rangeend"]
BASEURL = config["baseurl"]
MANUSCRIPTID = sys.argv[1]
TARGETDIR = BASEDIR + '/' + MANUSCRIPTID

missingfiles = []

rs = ['f{:03d}r.jpg'.format(x) for x in range(RANGEBEGIN,RANGEEND+1)]
vs = ['f{:03d}v.jpg'.format(x) for x in range(RANGEBEGIN,RANGEEND+1)]

allfiles = rs + vs
downloaded = os.listdir(TARGETDIR)

missingfiles = list(set(allfiles).difference(set(downloaded)))
missingfiles.sort()
s = requests.Session()

while len(missingfiles) > 0:
   #candidate = random.sample(missingfiles,1)[0]
   candidate = missingfiles[0]
   trydownload(candidate)
   updatedownloaded(downloaded,candidate)
   if candidate in downloaded:
       missingfiles.remove(candidate)
       print('{} downloaded successfully'.format(candidate))
   print('Sleeping ...')
   for i in range(SLEEPTIME//5):
       print('.',end='',flush=True)
       time.sleep(5)
   print(' ')

