import PIL
from PIL import Image
import imagehash
f=open('filenames','r')
f1=open('imagehash','w')
for i in f:
  lenna = PIL.Image.open(i[:-1])
  ph=imagehash.phash(lenna)
  ah=imagehash.average_hash(lenna)
  dh=imagehash.dhash(lenna)
  f1.write(str(ph)+","+str(ah)+","+str(dh)+","+i)



import PIL
from PIL import Image
import imagehash
f=open('filenames','r')
f1=open('imagehash','w')

lenna = PIL.Image.open("01p5Y0ufdbL._SL160_.jpg")
ph=imagehash.phash(lenna)
  ah=imagehash.average_hash(lenna)
  dh=imagehash.dhash(lenna)
  print str(ph)+","+str(ah)+","+str(dh)+","
  avgph=int(str(ph))
  print avgph




f=open('imagehash','r')
import re
from polls.models import amznitems
count=0
for i in f: 
    a=re.match(r'(.*),(.*),(.*),(.*)',i)
    if a:
       print a.group(1)
       print a.group(4)
       b=amznitems.objects.filter(amzimg__icontains=a.group(4)).all() 
       for i in b:
           count=count+1
           print count
           i.ahash=a.group(2)
           i.phash=a.group(1)
           i.dhash=a.group(3) 
           i.save()    
    
