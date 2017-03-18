import os
from subprocess import call
for i in range (2,17):
   f=open("catval/catval"+str(i),'r')
   count=0
   if not os.path.exists("catval"+str(i)):
    os.makedirs("catval"+str(i))
   for j in f:
       fn=j[:-1]
       if len(fn)>4:
          count=count+1
          call(['curl',fn,'-o',"catval"+str(i)+"/a"+str(count)+".jpg"])
   
from polls.models import amznitems,flipitems,infiitems
import os
from subprocess import call
cate=['Laptop backpack','rucksacks','school bags','cabin luggage','wallet for men','messenger bags','tote bags','travel duffles','briefcases','wallet for women','handbags','slingbags']
import re
f1=open("err1",'w')
f2=open("err2",'w')
f3=open("fllinks",'w')
flst=[]
f4=open("tempalltypes",'r')
for i in f4:
   text=i
   donlst=i.split(",,")


count=0
for i in cate:
    print i
    a=flipitems.objects.filter(brandcategory__icontains=i.replace(" ","_")).all()
    for j in a:
       if j.amzimg.strip():
          fng=re.match(r'.*/(.*\.jpeg)',j.amzimg)
          if fng:
            if fng.group(1) in text:
                count=count+1
                continue
            fn="flimages/"+fng.group(1)
            flst.append([fn,j.amzimg])
            f3.write(j.amzimg+'\n')
          else:
              f1.write(j.amzimg+"\n")
       else:
           f2.write(j.id+"\n")  

f4=open("tempalltypes",'r')
for i in f4:
   donlst=i.split(",,")
for fn in flst:
  if not os.path.isfile(fn[0]) :
              call(['curl',fn[1],'-o',fn[0]])








from polls.models import amznitems,flipitems,infiitems,snapitems
import os
from subprocess import call
cate=['travel duffles','briefcases','wallet for women','handbags','slingbags']
import re
f1=open("err1",'w')
f2=open("err2",'w')
flst=[]
if 1:
    a=snapitems.objects.filter().all()
    for j in a:
       imgs=j.amzimg.split(",")
       if imgs:
          imgs[0]=imgs[0][1:-1]
          fng=re.match(r'.*/(.*\.jpg)',imgs[0])
          if fng:
            fn="snapimages/"+fng.group(1)
            
            flst.append([fn, imgs[0]])
          else:
              f1.write(j.amzimg+"\n")
       else:
           f2.write(j.id+"\n")  


for fn in flst:
  if not os.path.isfile(fn[0]):
              call(['curl',fn[1],'-o',fn[0]])


from polls.models import amznitems,flipitems,infiitems,ptmitems
import os
from subprocess import call
cate=['travel duffles','briefcases','wallet for women','handbags','slingbags']
import re
f1=open("err1",'w')
f2=open("err2",'w')
flst=[]
if 1:
    a=ptmitems.objects.filter().all()
    for j in a:
       if j.amzimg.strip():
          fng=re.match(r'https://assetscdn.paytm.com/images/catalog/product/(.*\.jpg)',j.amzimg)
          if fng:
            fn="ptmimages/"+fng.group(1).replace("/",".")
            
            flst.append([fn, j.amzimg])
          else:
              f1.write(j.amzimg+"\n")
       else:
           f2.write(j.id+"\n")  


for fn in flst:
  if not os.path.isfile(fn[0]):
              call(['curl',fn[1],'-o',fn[0]])
