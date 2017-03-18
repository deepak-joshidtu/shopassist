from django.http import HttpResponse
from .models import myCollection3
from polls.models import flipitems
from django.template import loader
from django.shortcuts import render
from django.db.models import Q
from django.db import DatabaseError
from .models import amznitems
from .models import amzntables
from .models import infiitems,ptmitems,snapitems,blogs
from .models import colorcounts
from django.http import HttpResponseNotFound
from .models import brandcounts
from difflib import SequenceMatcher as SM
from datetime import datetime
import re
def index(request):
    catet1=['Messenger Bags','Laptop Backpacks','Rucksacks','School Bags','Cabin Luggage','ToteBbags','Travel Duffles','Travel Accessories','Briefcases','Wallet for Women','Handbags','Slingbags']
    cateimgs=['http://ecx.images-amazon.com/images/I/41XdPx32kvL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/413Ahn89wrL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/51Yg7PAmK0L._AC_UL246_SR190,246_.jpg' ,'http://ecx.images-amazon.com/images/I/41ug3NXVvqL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41HPNlWFkdL._AC_UL246_SR190,246_.jpg' ,
'https://images-eu.ssl-images-amazon.com/images/I/41q2OjAlU9L._SL260_.jpg','http://ecx.images-amazon.com/images/I/41iDncnPOyL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41vGGhKQiwL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/51vnaQ2JGoL._AC_UL246_SR190,246_.jpg','https://images-eu.ssl-images-amazon.com/images/I/51BsUtYZGRL._SL260_.jpg','http://ecx.images-amazon.com/images/I/417PsjAihZL._AC_UL260_SR200,260_.jpg','http://ecx.images-amazon.com/images/I/41ReiAOMZ1L._AC_UL260_SR200,260_.jpg']
    catet1=['Briefcases','Wallet for Women','Messenger Bags','Laptop Backpacks','Rucksacks','School Bags','Cabin Luggage','ToteBbags','Travel Duffles','Travel Accessories','Handbags','Slingbags']
    cateimgs=['http://ecx.images-amazon.com/images/I/51vnaQ2JGoL._AC_UL246_SR190,246_.jpg','https://images-eu.ssl-images-amazon.com/images/I/51BsUtYZGRL._SL260_.jpg','http://ecx.images-amazon.com/images/I/41XdPx32kvL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/413Ahn89wrL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/51Yg7PAmK0L._AC_UL246_SR190,246_.jpg' ,'http://ecx.images-amazon.com/images/I/41ug3NXVvqL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41HPNlWFkdL._AC_UL246_SR190,246_.jpg' ,
'https://images-eu.ssl-images-amazon.com/images/I/41q2OjAlU9L._SL260_.jpg','http://ecx.images-amazon.com/images/I/41iDncnPOyL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41vGGhKQiwL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/417PsjAihZL._AC_UL260_SR200,260_.jpg','http://ecx.images-amazon.com/images/I/41ReiAOMZ1L._AC_UL260_SR200,260_.jpg']

#teimgs=['http://ecx.images-amazon.com/images/I/41XdPx32kvL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/413Ahn89wrL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/51Yg7PAmK0L._AC_UL246_SR190,246_.jpg' ,'http://ecx.images-amazon.com/images/I/41ug3NXVvqL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41HPNlWFkdL._AC_UL246_SR190,246_.jpg' ,
#'http://ecx.images-amazon.com/images/I/41Lff8oitLL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41iDncnPOyL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41vGGhKQiwL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/51vnaQ2JGoL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41nnRhGmCYL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/417PsjAihZL._AC_UL260_SR200,260_.jpg','http://ecx.images-amazon.com/images/I/41ReiAOMZ1L._AC_UL260_SR200,260_.jpg']

    count=0
    cate1=[]
    cate2={'cate11':'','cate1':'','cate21':'','cate2':'','cateimgs':'','cateimgs1':''}
    cateimgs1=[]
    cateimgs2=[]
    cate=['briefcases','wallet for women','messenger bags','Laptop backpacks','rucksacks','school bags','cabin luggage','tote bags','travel duffles','travel accessories','handbags','slingbags']
   # cate=[3,0,5,6,1,9,2,11,4,10,7,8]
    for i in cate:
        if count%2==0:
            cate2={'cate11':catet1[count],'cate1':str(i),'cate21':catet1[count+1],'cate2':str(cate[count+1]),'cateimg1':cateimgs[count],'cateimg2':cateimgs[count+1]}

        #    cate2={'cate11':cate1[count],'cate1':str(i),'cate21':cate1[count+1],'cate2':str(cate[count+1]),'cateimg1':cateimgs[count],'cateimg2':cateimgs[count+1]}
            cate1.append(cate2)
        count=count+1
    context={'category':cate1,}
    return render(request, 'polls/home1.html',context)
def gameindex(request):
    catet1=['Briefcases','Wallet for Women','Messenger Bags','Laptop Backpacks','Rucksacks','School Bags','Cabin Luggage','ToteBbags','Travel Duffles','Travel Accessories','Handbags','Slingbags']
    cateimgs=['http://ecx.images-amazon.com/images/I/51vnaQ2JGoL._AC_UL246_SR190,246_.jpg','https://images-eu.ssl-images-amazon.com/images/I/51BsUtYZGRL._SL260_.jpg','http://ecx.images-amazon.com/images/I/41XdPx32kvL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/413Ahn89wrL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/51Yg7PAmK0L._AC_UL246_SR190,246_.jpg' ,'http://ecx.images-amazon.com/images/I/41ug3NXVvqL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41HPNlWFkdL._AC_UL246_SR190,246_.jpg' ,
'https://images-eu.ssl-images-amazon.com/images/I/41q2OjAlU9L._SL260_.jpg','http://ecx.images-amazon.com/images/I/41iDncnPOyL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41vGGhKQiwL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/417PsjAihZL._AC_UL260_SR200,260_.jpg','http://ecx.images-amazon.com/images/I/41ReiAOMZ1L._AC_UL260_SR200,260_.jpg']
#teimgs=['http://ecx.images-amazon.com/images/I/41XdPx32kvL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/413Ahn89wrL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/51Yg7PAmK0L._AC_UL246_SR190,246_.jpg' ,'http://ecx.images-amazon.com/images/I/41ug3NXVvqL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41HPNlWFkdL._AC_UL246_SR190,246_.jpg' ,
#'http://ecx.images-amazon.com/images/I/41Lff8oitLL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41iDncnPOyL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41vGGhKQiwL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/51vnaQ2JGoL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41nnRhGmCYL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/417PsjAihZL._AC_UL260_SR200,260_.jpg','http://ecx.images-amazon.com/images/I/41ReiAOMZ1L._AC_UL260_SR200,260_.jpg']

    count=0
    cate1=[]
    cate2={'cate11':'','cate1':'','cate21':'','cate2':'','cateimgs':'','cateimgs1':''}
    cateimgs1=[]
    cateimgs2=[]
    cate=['messenger bags','Laptop backpacks','rucksacks','school bags','cabin luggage','tote bags','travel duffles','travel accessories','briefcases','wallet for women','handbags','slingbags']
   # cate=[3,0,5,6,1,9,2,11,4,10,7,8]
    for i in cate:
        if count%2==0:
            cate2={'cate11':catet1[count],'cate1':str(i),'cate21':catet1[count+1],'cate2':str(cate[count+1]),'cateimg1':cateimgs[count],'cateimg2':cateimgs[count+1]}

        #    cate2={'cate11':cate1[count],'cate1':str(i),'cate21':cate1[count+1],'cate2':str(cate[count+1]),'cateimg1':cateimgs[count],'cateimg2':cateimgs[count+1]}
            cate1.append(cate2)
        count=count+1
    context={'category':cate1,}
    return render(request, 'polls/gamehome.html',context)

from bs4 import BeautifulSoup
import urllib2
def getprice(request,pid):
   headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
   }
   price=" "
   osource="amazon"
   sgrp=[]
   flgrp=[]
   snapgrp=[]
   infigrp=[]
   ptmgrp=[]
   pdct=amznitems.objects.filter(id=pid).all()[0]
   if pdct.pdgrp >0:
       grp=amznitems.objects.filter(pdgrp=pdct.pdgrp).all()
       flgrp=flipitems.objects.filter(pdgrp=pdct.pdgrp).all()
       spgrp=snapitems.objects.filter(pdgrp=pdct.pdgrp).all()
       igrp=infiitems.objects.filter(pdgrp=pdct.pdgrp).all()
       pgrp=ptmitems.objects.filter(pdgrp=pdct.pdgrp).all()
       for i in grp:
     #    if i.id not in pdct.id:
              sgrp.append(i)
   else:
        sgrp.append(pdct)
   prc=""
   print sgrp
   for i in sgrp:
     dtt=datetime.now()
     if (dtt-i.created).total_seconds()>100:
       i.created=datetime.now() 
       url="http://www.amazon.in/gp/product/"+i.asin
       print url
       reqt = urllib2.Request(url, headers=headers)
       reqt1=urllib2.urlopen(reqt)
       br=BeautifulSoup(reqt1.read())
       pr = br.findAll("span", {'id':"priceblock_ourprice"})
       if pr:
        price=pr[0].text
        price=price.replace(",","")
        prc+=price+","
        i.cprice=price
        i.save()
        continue
       pr = br.findAll("span", {'id':"priceblock_saleprice"})
       if pr:
         price=pr[0].text
         price=price.replace(",","")
         prc+=price
         i.cprice=price
         i.save()
         continue
       prc+=","
     else:
        prc+=i.cprice +","
     
   for i in flgrp:
       print prc
       dtt=datetime.now()
       if (dtt-i.created).total_seconds()>1:
         i.created=datetime.now()
         url=i.amzlink.replace("&affid=myselfdjo","")
         print url
         reqt = urllib2.Request(url, headers=headers)
         reqt1=urllib2.urlopen(reqt)
         #br=BeautifulSoup(reqt1.read())
         #pr = br.findAll("script", {'id':"is_script"})
         if 1:
          b=reqt1.read()
         # pcont=pr[0].text
          bsp=b.split("\"price\":")
          price=re.match("([0-9]*).*",bsp[1])
          if price:
             prc+=price.group(1)+","
             i.cprice=price.group(1)
             i.save()
          else:
             prc+=","
       else:
          prc+=i.cprice +","

   context={'price':prc,}
   return render(request,'polls/price.html',context)

def blogsid(request,pid):
     bl1=blogs.objects.filter(id=pid).all()
     bl=[]
     for i in bl1:
        cnt=i.btext.split("\n")
        bl.append({'cnt':cnt,'bl':i})
     context={'bl':bl,}
     return render(request,'polls/blog.html',context)
      
def blog(request):
     bl1=blogs.objects.filter().all()
     bl=[]
     for i in bl1:
        i.btext=i.btext[:400]+"..."
        cnt=i.btext.split("\n")
        bl.append({'cnt':cnt,'bl':i})
     context={'bl':bl,}
     return render(request,'polls/blog.html',context)
def addcomplist(request):
    return render(request,'polls/blog.html')
def complist(request):
    ids=request.POST['ids']
    k=ids.split(",")
    row=[]
    for i in k:
      if len(i)>3:
       print i
       qi=amznitems.objects.filter(id=i).all()
       if qi:
          row.append(qi[0])
    context = {
  
        'row': row,
        }
    return render(request,'polls/compall.html',context)


    
def productdetail(request,pdctid):
    
    try : pdct=amznitems.objects.filter(id=pdctid).all()[0]
    except DatabaseError:
        return HttpResponseNotFound('<h1>Product not found</h1>')

    if not pdct:
       return HttpResponseNotFound('<h1>Product not found</h1>')     
    simpro=amznitems.objects.filter(brandcategory=pdct.brandcategory,price__lte=pdct.price+400,price__gte=pdct.price-400,dispscore__gte=0).order_by('-dispscore').all()[:18]
    pdctsame=amznitems.objects.filter(spid=pdctid).all()
    n1=pdct.amzlink
    feakey=pdct.feakey.split(",")
    name=re.match(r'.*\.in/(.*)/dp.*',n1).group(1)
    imgs=[]
    if(len(pdct.amzimg0)>4):imgs.append(pdct.amzimg0)
    if(len(pdct.amzimg1) >4):imgs.append(pdct.amzimg1)
    if(len(pdct.amzimg2)>4):imgs.append(pdct.amzimg2)
    if(len(pdct.amzimg3)>4):imgs.append(pdct.amzimg3)
    if(len(pdct.amzimg4)>4):imgs.append(pdct.amzimg4)
    sgrp=[]
    flgrp=[]
    snapgrp=[]
    infigrp=[]
    ptmgrp=[]
    if pdct.pdgrp >0:
       grp=amznitems.objects.filter(pdgrp=pdct.pdgrp).all()
       fgrp=flipitems.objects.filter(pdgrp=pdct.pdgrp).all()
       spgrp=snapitems.objects.filter(pdgrp=pdct.pdgrp).all()
       igrp=infiitems.objects.filter(pdgrp=pdct.pdgrp).all()
       pgrp=ptmitems.objects.filter(pdgrp=pdct.pdgrp).all()
       count=0
       for i in grp:
     #    if i.id not in pdct.id:
              count=count+1
              sg={'sgrp':i,'count':count}
              sgrp.append(sg)
       for i in fgrp:
     #    if i.id not in pdct.id:
              count=count+1
              sg={'sgrp':i,'count':count}
              flgrp.append(sg)
       for i in spgrp:
     #    if i.id not in pdct.id:
              count=count+1
              sg={'sgrp':i,'count':count}
              snapgrp.append(sg)
       for i in igrp:
     #    if i.id not in pdct.id:
              count=count+1
              sg={'sgrp':i,'count':count}
              infigrp.append(sg)
       for i in pgrp:
     #    if i.id not in pdct.id:
              count=count+1
              sg={'sgrp':i,'count':count}
              ptmgrp.append(sg)

    else:
        sgrp.append({'sgrp':pdct,'count':1})
       
    context = {
        'pdct': pdct,
        'name':name,
        'imgs':imgs,
         'pdctsame':pdctsame,
        'sgrp':sgrp,
        'flgrp':flgrp,
        'snapgrp':snapgrp,
        'infigrp':infigrp,
        'ptmgrp':ptmgrp,
        'feakey':feakey[:-1],
        'simpro':simpro,
            }
    return render(request, 'polls/productdetail.html',context)


def tcolor(request,category):
    queryitems1=[[],[],[],[],[],[]]
    queryitems=[]
    namelist=[]
    #cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
    colorlst=[]
    count=0
    count1=0
    wrapper=[[],[],[],[],[],[]]
    colitems=[]
    cols=['pink','red','orange','yellow','brown','green','cyan','blue','indigo','purple','violet','magenta','white','gray','black']
    for i in cols:
       brndcats=amznitems.objects.filter(brandcategory__icontains=category.replace(" ","_"),color__icontains=i).all()
       if brndcats:
                          # colitems.append(brndcats[0].colorcount)
                          # colorlst.append(k.color)
                           k=brndcats[0]
                           k.color=i
                           k.amzimg=k.amzimg.replace('SL160','SL260')
                           queryitems1[count%6].append(k)
                           count=count+1
                        
    context = {
        
        'row': queryitems1,
        'category': category,
        }

    return render(request, 'polls/tlhome5.html',context)

def catecolor(request,category,color):
    allcolors=['red','blue','green','purple','orange','grey','black']
    queryitems1=[[],[],[],[],[],[]]
    queryitems=[]
    namelist=[]
    imglst=[]
    colorlst=[]
    count=0
    count1=0
    cate={'messenger bags':3,'Laptop backpacks':0,'rucksacks':5,'school bags':6,'cabin luggage':1,'tote bags':9,'travel duffles':2,'travel accessories':11,'briefcases':4,'wallet for women':10,'handbags':7,'slingbags':8,'wallet for men':12}
   # cate=[3,0,5,6,1,9,2,11,4,10,7,8]
    #catlist=[[1,2],[4,5],[6,7],[8,9],[10,11],[12],[13],[14],[15],[16],[17],[18]]
    catlitval=[[{'tex':'good quality','val':1},{'tex':'quality not sure','val':2}],[{'tex':'solid','val':4},{'tex':'garment','val':5}],[{'tex':'NoWheels','val':6},{'tex':'Wheels','val':7}],[{'tex':'casual','val':8},{'tex':'official','val':9}],[{'tex':'solid','val':10},{'tex':'garment','val':11}],[],[],[],[],[],[],[],[]]
    #sbcats=catlist[int(category)]
    #if len(sbcats)==1:
     #  brndcats=amznitems.objects.filter(catval=sbcats[0]).order_by('dispscore').all()
    #if len(sbcats)==2:
     #  brndcats=amznitems.objects.filter(Q(catval=sbcats[0])|Q(catval=sbcats[1])).order_by('dispscore').all()
    catlstv=catlitval[cate[category]]

    brndcats=amznitems.objects.filter(brandcategory__icontains=category.replace(" ","_"),color__icontains=color).order_by('-dispscore').all()
    for k in brndcats:
              #   if color in k.color or k.color in color:
#                       colorlst.append(k.color)
                       count=count+1
                       k.title=k.title[:20]+".."
                       k.amzimg=k.amzimg.replace('SL160','SL260')
                       queryitems.append(k)
    th=len(queryitems)/6
    count=0
    count1=0
    for i in queryitems:
        if count1>5:
            count1=0
        queryitems1[count1].append(i)
        count1=count1+1
    lt=len(queryitems)
    row1=queryitems1
    context = {
        'row': row1,
        'category': category,
        'catlst':catlstv,
        'color': color,
        'colorn':color,
        }
  

    return render(request, 'polls/coloritems.html',context)
def catebrandc(request,category,brand,colr):
    queryitems1=[[],[],[],[],[],[],[],[],[],[],[],[]]
    queryitems=[]
    namelist=[]
    imglst=[]
    colorlst=[]
    count=0
    count1=0
    brnd=[]
    lid=[]
    pdgrp=[]
    brndcats=amznitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).order_by('price').all()
    brndcatsf=flipitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).order_by('price').all()
    brndcatsi=infiitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    brndcatss=snapitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    brndcatsp=ptmitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()


    cols=['pink','red','orange','yellow','brown','green','cyan','blue','indigo','purple','violet','magenta','white','gray','black']


    for k in  brndcats:
        if k.amzimg not in imglst and k.catval!=0:#and k.blk==0:# and k.spid not in lid  :
#            if k.pdgrp not in pdgrp:
            if colr=="others":
                p=0
                for i in cols:
                    if i[1:] in k.color:
                       p=1
                if p==0:
                 pdgrp.append(k.pdgrp)
                 imglst.append(k.amzimg)
                 lid.append(k.id)
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems.append(k)
                continue
   
            if colr[1:] in k.color:
                 pdgrp.append(k.pdgrp)
                 imglst.append(k.amzimg)
                 lid.append(k.id)
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems.append(k)
    if brndcatsf:
      for k in brndcatsf:
            if k.amzimg not in imglst and k.blk==0 and k.spid not in lid:
              if colr=="others":
                p=0
                for i in cols:
                    if i[1:] in k.color:
                       p=1
                if p==0:
                 imglst.append(k.amzimg)
                 lid.append(k.id)
                 queryitems.append(k)
                continue

              if colr[1:] in k.color:
                 imglst.append(k.amzimg)
                 lid.append(k.id)
#                      colorlst.append(k.color)
                 queryitems.append(k)
 #   brndcats=infiitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    for k in brndcatsi:
        k.osource="infibeam"
        a=k.amzimg.split(",")
        if a:
           k.amzimg=a[0]
        if k.amzimg not in imglst  and k.spid not in lid:
            if colr=="others":
                p=0
                for i in cols:
                    if i in k.allkeyw:
                       p=1
                if p==0:
                 imglst.append(k.amzimg)
                 lid.append(k.id)
                 queryitems.append(k)
                continue

            if colr in k.allkeyw:
                 imglst.append(k.amzimg)

                 queryitems.append(k)
#    brndcats=snapitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    for k in brndcatss:
        a=k.amzimg.split(",")
        k.price="unknown"
        k.osource="snapdeal"
        if a:
           k.amzimg=a[0]
        if k.amzimg not in imglst  and k.spid not in lid:
            if colr=="others":
                p=0
                for i in cols:
                    if i in k.allkeyw:
                       p=1
                if p==0:
                 imglst.append(k.amzimg)
                 lid.append(k.id)
                 queryitems.append(k)
                continue

            if colr in k.allkeyw:

                 imglst.append(k.amzimg)

                 queryitems.append(k)
 #   brndcats=ptmitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    for k in brndcatsp:
        a=k.amzimg.split(",")
        if a:
           k.amzimg=a[0]
        if k.amzimg not in imglst  and k.spid not in lid:
            if colr=="others":
                p=0
                for i in cols:
                    if i in k.allkeyw:
                       p=1
                if p==0:
                 imglst.append(k.amzimg)
                 k.osource="paytm"
                 queryitems.append(k)
                continue


            if colr in k.allkeyw:

                 imglst.append(k.amzimg)

                 k.osource="paytm"
                 queryitems.append(k)

    th=len(queryitems)/12
    count=0
    count1=0
    for i in queryitems:
        if count1>11:
            count1=0
        queryitems1[count1].append(i)
        count1=count1+1
    lt=len(queryitems)
    row1=queryitems1

    context = {
         'brand':brand,
        'row': row1,
        'category': category,
        }

    return render(request, 'polls/matchitems.html',context)


                                                            
def catebrand(request,category,brand):
    queryitems1=[[],[],[],[],[],[],[],[],[],[],[],[]]
    queryitems=[]
    namelist=[]
    imglst=[]
    colorlst=[]
    count=0
    count1=0
    brnd=[]
    lid=[]
    pdgrp=[]
    brndcats=amznitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).order_by('price').all()
    brndcatsf=flipitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).order_by('price').all()
    brndcatsi=infiitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    brndcatss=snapitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    brndcatsp=ptmitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    

    cols=['pink','red','orange','yellow','brown','green','cyan','blue','indigo','purple','violet','magenta','white','gray','black'] 


    for k in  brndcats:
        if k.amzimg not in imglst and k.catval!=0:#and k.blk==0:# and k.spid not in lid  :
#            if k.pdgrp not in pdgrp:
                 pdgrp.append(k.pdgrp)
                 imglst.append(k.amzimg)
                 lid.append(k.id)
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems.append(k)
                 for i in cols:
                     if i in k.color:
                          for j in brndcatss:
                              if i in j.allkeyw:
                                   a=j.amzimg.split(",")
                                   j.price="unknown"
                                   j.osource="snapdeal"
                                   if a:
                                       j.amzimg=a[0]
                                   if j.amzimg not in imglst  and j.spid not in lid:
                                      imglst.append(j.amzimg)
                                      lid.append(j.id)
#                      colorlst.append(k.color)
                                      queryitems.append(j)
                          for j in brndcatsi:
                              if i in j.allkeyw:
                                   a=j.amzimg.split(",")
#                                   j.price="unknown"
                                   j.osource="infibeam"
                                   if a:
                                       j.amzimg=a[0]
                                   if j.amzimg not in imglst  and j.spid not in lid:
                                      imglst.append(j.amzimg)
                                      lid.append(j.id)
#                      colorlst.append(k.color)
                                      queryitems.append(j)
                          for j in brndcatsf:
                              if i in j.color:
                                   if j.amzimg not in imglst  and j.spid not in lid:
                                      imglst.append(j.amzimg)
                                      lid.append(j.id)
#                      colorlst.append(k.color)
                                      queryitems.append(j)
                          for j in brndcatsp:
                              if i in j.allkeyw:
                                   a=j.amzimg.split(",")
                                   #j.price="unknown"
                                   j.osource="paytm"
                                   if a:
                                       j.amzimg=a[0]
                                   if j.amzimg not in imglst  and j.spid not in lid:
                                      imglst.append(j.amzimg)
                                      lid.append(j.id)
#                      colorlst.append(k.color)
                                      queryitems.append(j)

 
#    brndcats=flipitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).order_by('price').all()
    if brndcatsf:
      for k in brndcatsf:
            if k.amzimg not in imglst and k.blk==0 and k.spid not in lid:
                 imglst.append(k.amzimg)
                 lid.append(k.id)
#                      colorlst.append(k.color)
                 queryitems.append(k)
 #   brndcats=infiitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    for k in brndcatsi:
        k.osource="infibeam"
        a=k.amzimg.split(",")
        if a:
           k.amzimg=a[0]
        if k.amzimg not in imglst  and k.spid not in lid:
                 imglst.append(k.amzimg)

                 queryitems.append(k)
#    brndcats=snapitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    for k in brndcatss:
        a=k.amzimg.split(",")
        k.price="unknown"
        k.osource="snapdeal"
        if a:
           k.amzimg=a[0]
        if k.amzimg not in imglst  and k.spid not in lid:
                 imglst.append(k.amzimg)

                 queryitems.append(k)
 #   brndcats=ptmitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    for k in brndcatsp:
        a=k.amzimg.split(",")
        if a:
           k.amzimg=a[0]
        if k.amzimg not in imglst  and k.spid not in lid:
                 imglst.append(k.amzimg)

                 k.osource="paytm"
                 queryitems.append(k)

        
    th=len(queryitems)/12
    count=0
    count1=0
    for i in queryitems:
        if count1>11:
            count1=0
        queryitems1[count1].append(i)
        count1=count1+1
    lt=len(queryitems)
    row1=queryitems1
   
    context = {
         'brand':brand,
        'row': row1,
        'category': category,
        }

    return render(request, 'polls/matchitems.html',context)
def sbcate(request,category,sbcat):
    queryitems1=[[],[],[],[],[],[]]
    queryitems=[]
    namelist=[]
    imglst=[]
    colorlst=[]
    count=0
    count1=0
    brnd=[]
    lid=[]
    pdgrp=[]
    brndcats=amznitems.objects.filter(catval=sbcat).all()
    for k in  brndcats:
        if k.amzimg not in imglst :#and k.blk==0:# and k.spid not in lid  :
    #        if k.pdgrp not in pdgrp:
                 pdgrp.append(k.pdgrp)
                 imglst.append(k.amzimg)
                 lid.append(k.id)
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems.append(k)
    brndcats=flipitems.objects.filter(catval=sbcat).all()
    if brndcats:
      for k in brndcats:
            if k.amzimg not in imglst and k.blk==0 and k.spid not in lid:
                 imglst.append(k.amzimg)
                 lid.append(k.id)
#                      colorlst.append(k.color)
                 queryitems.append(k)

    th=len(queryitems)/6
    count=0
    count1=0
    for i in queryitems:
        if count1>5:
            count1=0
        queryitems1[count1].append(i)
        count1=count1+1
    lt=len(queryitems)
    row1=queryitems1
    context = {
         'brand':sbcat,
        'row': row1,
        'category': category,
        }

    return render(request, 'polls/matchitems.html',context)
def cateprice(request,category,p1,p2):
    queryitems1=[[],[],[],[],[],[]]
    queryitems=[]
    namelist=[]
    imglst=[]
    colorlst=[]
    count=0
    count1=0
    brnd=[]
    lid=[]
    pdgrp=[]
    brndcats=amznitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    for k in  brndcats:
        if k.amzimg not in imglst and k.catval!=0:# and k.blk==0:# and k.spid not in lid  :
    #        if k.pdgrp not in pdgrp:
                 pdgrp.append(k.pdgrp)
                 imglst.append(k.amzimg)
                 lid.append(k.id)
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems.append(k)
    brndcats=flipitems.objects.filter(brandcategory__icontains=brand.replace(" ","")).all()
    if brndcats:
      for k in brndcats:
            if k.amzimg not in imglst and k.blk==0 and k.spid not in lid:
                 imglst.append(k.amzimg)
                 lid.append(k.id)
#                      colorlst.append(k.color)
                 queryitems.append(k)

    th=len(queryitems)/6
    count=0
    count1=0
    for i in queryitems:
        if count1>5:
            count1=0
        queryitems1[count1].append(i)
        count1=count1+1
    lt=len(queryitems)
    row1=queryitems1
    context = {
         'brand':brand,
        'row': row1,
        'category': category,
        }

    return render(request, 'polls/matchitems.html',context)

def catebrand1(request,category,brand):
    queryitems1=[[],[],[],[],[],[]]
    queryitems=[]
    namelist=[]
    cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
    colorlst=[]
    count=0
    count1=0
    th=len(cats)/6
    brnd=[]
    cate={'messenger bags':3,'Laptop backpacks':0,'rucksacks':5,'school bags':6,'cabin luggage':1,'tote bags':9,'travel duffles':2,'travel accessories':11,'briefcases':4,'wallet for women':10,'handbags':7,'slingbags':8,'wallet for men':12}
   # cate=[3,0,5,6,1,9,2,11,4,10,7,8]
    #catlist=[[1,2],[4,5],[6,7],[8,9],[10,11],[12],[13],[14],[15],[16],[17],[18]]
    catlitval=[[{'tex':'good quality','val':1},{'tex':'quality not sure','val':2}],[{'tex':'solid','val':4},{'tex':'garment','val':5}],[{'tex':'NoWheels','val':6},{'tex':'Wheels','val':7}],[{'tex':'casual','val':8},{'tex':'official','val':9}],[{'tex':'solid','val':10},{'tex':'garment','val':11}],[],[],[],[],[],[],[],[]]
    #sbcats=catlist[int(category)]
    #if len(sbcats)==1:
     #  brndcats=amznitems.objects.filter(catval=sbcats[0]).order_by('dispscore').all()
    #if len(sbcats)==2:
     #  brndcats=amznitems.objects.filter(Q(catval=sbcats[0])|Q(catval=sbcats[1])).order_by('dispscore').all()
    catlstv=catlitval[cate[category]]
    imghsh=[]
    q=category.replace(" ","_")+brand.replace(" ","")
    brndcats=amznitems.objects.filter(brandcategory__icontains=q).order_by('-dispscore').all()
    for k in brndcats:
    #        if k.amzimg not in imglst and k.catval!=0:
     #            imglst.append(k.amzimg)
      #           if brand in k.brand or k.brand in brand:
#                      colorlst.append(k.color)
       #                count=count+1
                if k.phash not in imghsh:
                       imghsh.append(k.phash)
                       k.title=k.title[:20]+".."
                       k.amzimg=k.amzimg.replace('SL160','SL260')
                       queryitems.append(k)
    th=len(queryitems)/6
    count=0
    count1=0
    for i in queryitems:
        if count1>5:
            count1=0
        queryitems1[count1].append(i)
        count1=count1+1
    lt=len(queryitems)
    row1=queryitems1

    context = {
         'brand':brand,
        'row': row1,
        'category': category,
          'catlst':catlstv,
             }

    return render(request, 'polls/coloritems.html',context)

                                          
def tbrand(request,category):
    queryitems1=[[],[],[],[],[],[]]
    queryitems=[]
    namelst=[]
    cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
    count=0
    count1=0
    brnd=[]
    th=len(cats)/6
    for i in cats:
        if(not i.tablename): continue
        brndcats=amznitems.objects.filter(brandcategory__icontains=i.tablename).all()
        if brndcats:
            k=brndcats[0]
            if k.amzimg not in imglst and k.blk==0:
                 brnd.append(k.brand)
                 imglst.append(k.amzimg)
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems.append(k)
                 name=" "
                 if re.match(category.replace(" ","_")+'(.*)',k.brandcategory):
                     name=re.match(category.replace(" ","_")+'(.*)',k.brandcategory).group(1)
                 namelst.append(name)
    th=len(queryitems)/6
    count=0
    count1=0
    for i in queryitems:
        if count1>5:
            count1=0
        queryitems1[count1].append(i)
        count1=count1+1
    cnt=0
    metab1="explore luggage online,explore bags online, "
    for i in brnd:
       if cnt>4:break
       cnt=cnt+1
       metab1=metab1+", "+i
    lt=len(queryitems)
    row1=queryitems1 
    context = {
        'metab1':metab1,
        'row': row1,
         'category': category,
        'name':namelst, 
        }

    return render(request, 'polls/thome44.html',context)

def tsbcate(request,category,sbcat):
    queryitems1=[[],[],[],[],[],[]]
    queryitems=[]
    namelst=[]
    cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
    count=0
    count1=0
    brnd=[]
    th=len(cats)/6
    for i in cats:
        if(not i.tablename): continue
        brndcats=amznitems.objects.filter(brandcategory__icontains=i.tablename).all()
        if brndcats:
            k=brndcats[0]
            if k.amzimg not in imglst and k.blk==0:
                 brnd.append(k.brand)
                 imglst.append(k.amzimg)
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems.append(k)
                 name=" "
                 if re.match(category.replace(" ","_")+'(.*)',k.brandcategory):
                     name=re.match(category.replace(" ","_")+'(.*)',k.brandcategory).group(1)
                 namelst.append(name)
    th=len(queryitems)/6
    count=0
    count1=0
    for i in queryitems:
        if count1>5:
            count1=0
        queryitems1[count1].append(i)
        count1=count1+1
    cnt=0
    metab1="explore bags online,explore luggage online "
    for i in brnd:
       if cnt>4:break
       cnt=cnt+1
       metab1=metab1+", "+i
    lt=len(queryitems)
    row1=queryitems1
    context = {
        'metab1':metab1,
        'row': row1,
         'category': category,
        'name':namelst,
        }

    return render(request, 'polls/thome44.html',context)

def tprice(request,category,p1,p2):
    queryitems1=[[],[],[],[],[],[]]
    queryitems=[]
    namelst=[]
  #  cats=amznitems.objects.filter(bagt__icontains=category).all()
    imglst=[]
    count=0
    count1=0
    brnd=[]
    #th=len(cats)/6
   # for i in cats:
    hashlst=[]
    brndcats=amznitems.objects.filter(brandcategory__icontains=category.replace(" ","_"),price__gte=p1,price__lte=p2).order_by('-dispscore').all()
    count1=0
    for k in brndcats:
        #    k=brndcats[0]
            if count>60: break
            if k.phash not in hashlst :
                 
                 hashlst.append(k.phash)
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems1[count%6].append(k)
                 count=count+1
    metab1="explore Luggage online,explore bags online"
    context = {
        'metab1':metab1,
        'row': queryitems1,
         'category': category,
        }

    return render(request, 'polls/byprice.html',context)



def tbrand1(request,category):
    queryitems1=[[],[],[],[],[],[]]
    queryitems=[]
    namelst=[]
    cats=amzntables.objects.filter(bagt__icontains=category).order_by('-brandcount').all()
    imglst=[]
    count=0
    count1=0
    brnd=[]
    wrapper=[[],[],[],[],[],[]]
    th=len(cats)/6
    brnd=['wildcraft','targus']
    for i in cats:
                 k=i
                 if count>60:break
                 k.amzimg=k.amzimg.replace('SL160','SL260') 
                 queryitems1[count%6].append(k)
                 count=count+1
    metab1="explore Luggage online,explore bags online"
    context = {
        'metab1':metab1,
        'row': queryitems1,
         'category': category,
        }

    return render(request, 'polls/tlhome4.html',context)

def detail(request, question_id):
    queryitems=[]
    namelist=[]
    brndcats=amznitems.objects.filter(brandcategory__icontains=u'Lenovo')
    queryitems.append(brndcats)
    for i in brndcats:
        name=re.match(r'.*\.in/(.*)/dp/.*',i.amzlink).group(1)
        namelist.append(name)
    context = {
        'row': brndcats,
        }
def tours1(request, category):
    queryitems=[]
    namelist=[]
    cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
    for i in cats:
        if(not i.tablename): continue
        brndcats=amznitems.objects.filter(brandcategory__icontains=i.tablename).all()
        count=0
        for k in brndcats:
            if k.amzimg not in imglst:
                 imglst.append(k.amzimg)
                 k.title=k.title[:20]+".."
                 k.amzimg=k.amzimg.replace('SL160','SL60')
                 queryitems.append(k)
                 name=re.match(r'.*\.in/(.*)/dp/.*',k.amzlink).group(1)
                 namelist.append(name)
    lt=len(queryitems)
    row11=queryitems[:lt/2]
    row1=row11[:100]
    row21=queryitems[lt/2:]    
    row2=row21[:100]
    context = {
        'row1': row1,
        'row2': row2,
        'category':category,
        }

#    return HttpResponse("doandfafa adf")
    return render(request,'polls/home3.html',context)
def sbtour(request, category,ccategory):
    queryitems=[]
    queryitems1=[[],[],[],[],[],[]]
    namelist=[]
    #cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
   # for i in cats:
   #     if(not i.tablename): continue

    cate={'messenger bags':3,'Laptop backpacks':0,'rucksacks':5,'school bags':6,'cabin luggage':1,'tote bags':9,'travel duffles':2,'travel accessories':11,'briefcases':4,'wallet for women':10,'handbags':7,'slingbags':8,'wallet for men':12}
   # cate=[3,0,5,6,1,9,2,11,4,10,7,8]
    catlist=[[1,2],[4,5],[6,7],[8,9],[10,11],[12],[13],[14],[15],[16],[17]]
    catlitval=[[{'tex':'good quality','val':1},{'tex':'quality not sure','val':2}],[{'tex':'solid','val':4},{'tex':'garment','val':5}],[{'tex':'NoWheels','val':6},{'tex':'Wheels','val':7}],[{'tex':'casual','val':8},{'tex':'official','val':9}],[{'tex':'solid','val':10},{'tex':'garment','val':11}],[],[],[],[],[],[],[]]
    #sbcats=catlist[int(category)]
    #if len(sbcats)==1:
     #  brndcats=amznitems.objects.filter(catval=sbcats[0]).order_by('dispscore').all()
    #if len(sbcats)==2:
     #  brndcats=amznitems.objects.filter(Q(catval=sbcats[0])|Q(catval=sbcats[1])).order_by('dispscore').all()
    count=0
    catlstv=catlitval[cate[ccategory]]
    brndcats=amznitems.objects.filter(catval=category).order_by('dispscore').all()
    count=0
    for k in brndcats:
            if k.amzimg not in imglst and k.blk==0 :
                 imglst.append(k.amzimg)
                 k.title=k.title[:20]+".."
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems.append(k)
                 name=re.match(r'.*\.in/(.*)/dp/.*',k.amzlink).group(1)
                 namelist.append(name)
    lt=len(queryitems)
    th=len(queryitems)/6
    count=0
    count1=0
    for i in queryitems[:60]:
        if count1>5:
            count1=0
        queryitems1[count1].append(i)
        count1=count1+1
    lt=len(queryitems)
    row1=queryitems1
    context = {
       'travelp':1,
        'row': row1,
        'category': ccategory,
        'catlst':catlstv,
        }
    return render(request,'polls/colorbrand.html',context)
def sbsbtour(request,ctype,cval, category,ccategory):
    queryitems=[]
    queryitems1=[[],[],[],[],[],[]]
    namelist=[]
    #cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
   # for i in cats:
   #     if(not i.tablename): continue

    cate={'messenger bags':3,'Laptop backpacks':0,'rucksacks':5,'school bags':6,'cabin luggage':1,'tote bags':9,'travel duffles':2,'travel accessories':11,'briefcases':4,'wallet for women':10,'handbags':7,'slingbags':8,'wallet for men':12}
   # cate=[3,0,5,6,1,9,2,11,4,10,7,8]
    #catlist=[[1,2],[4,5],[6,7],[8,9],[10,11],[12],[13],[14],[15],[16],[17],[18]]
    count=0
    cats=10
    catlitval=[[{'tex':'good quality','val':1},{'tex':'quality not sure','val':2}],[{'tex':'solid','val':4},{'tex':'garment','val':5}],[{'tex':'NoWheels','val':6},{'tex':'Wheels','val':7}],[{'tex':'casual','val':8},{'tex':'official','val':9}],[{'tex':'solid','val':10},{'tex':'garment','val':11}],[],[],[],[],[],[],[],[]]
    #sbcats=catlist[int(category)]
    #if len(sbcats)==1:
     #  brndcats=amznitems.objects.filter(catval=sbcats[0]).order_by('dispscore').all()
    #if len(sbcats)==2:
     #  brndcats=amznitems.objects.filter(Q(catval=sbcats[0])|Q(catval=sbcats[1])).order_by('dispscore').all()
    catlstv=catlitval[cate[ccategory]]

    count=0
    categ=ccategory
#    for i in catlist:
 #      for j in i:
  #        if j==int(category):
   #         catlstv=catlitval[count]
    #        categ=cate[count]
    #   count=count+1
    if (ctype=='brand'):
       color=""
       brand=cval
       brndcats=amznitems.objects.filter(brandcategory__icontains=cval.replace(" ",""),catval=category).order_by('dispscore').all()
    else:
       brand=""
       color=cval
       brndcats=amznitems.objects.filter(color__icontains=cval,catval=category).order_by('dispscore').all()

    count=0
    for k in brndcats:
            if k.amzimg not in imglst and k.blk==0 :
                 k.title=k.title[:20]+".."
                 imglst.append(k.amzimg)
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems.append(k)
                 name=re.match(r'.*\.in/(.*)/dp/.*',k.amzlink).group(1)
                 namelist.append(name)
    lt=len(queryitems)
    th=len(queryitems)/6
    count=0
    count1=0
    for i in queryitems[:60]:
        if count1>5:
            count1=0
        queryitems1[count1].append(i)
        count1=count1+1
    lt=len(queryitems)
    row1=queryitems1
    context = {
        'color':color,
        'brand':brand, 
        'row': row1,
        'category': categ,
        'catlst':catlstv,
        }
    return render(request,'polls/coloritems.html',context)

def tours(request, category):
    queryitems=[]
    queryitems1=[[],[],[],[],[],[]]
    namelist=[]
    #cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
   # for i in cats:
   #     if(not i.tablename): continue
    cate={'messenger bags':3,'Laptop backpacks':0,'rucksacks':5,'school bags':6,'cabin luggage':1,'tote bags':9,'travel duffles':2,'travel accessories':11,'briefcases':4,'wallet for women':10,'handbags':7,'slingbags':8,'wallet for men':12}
   # cate=[3,0,5,6,1,9,2,11,4,10,7,8]
    #catlist=[[1,2],[4,5],[6,7],[8,9],[10,11],[12],[13],[14],[15],[16],[17],[18]]
    catlitval=[[{'tex':'good quality','val':1},{'tex':'quality not sure','val':2}],[{'tex':'solid','val':4},{'tex':'garment','val':5}],[{'tex':'NoWheels','val':6},{'tex':'Wheels','val':7}],[{'tex':'casual','val':8},{'tex':'official','val':9}],[{'tex':'solid','val':10},{'tex':'garment','val':11}],[],[],[],[],[],[],[],[]]
    #sbcats=catlist[int(category)]
    #if len(sbcats)==1:
     #  brndcats=amznitems.objects.filter(catval=sbcats[0]).order_by('dispscore').all()
    #if len(sbcats)==2:
     #  brndcats=amznitems.objects.filter(Q(catval=sbcats[0])|Q(catval=sbcats[1])).order_by('dispscore').all()
    catlstv=catlitval[cate[category]]
    count=0
    q=category.replace(" ","_")
    brndcats=amznitems.objects.filter(brandcategory__icontains=q).order_by('-dispscore').all()
   # brndcats.sort(key=lambda x: x.dispscore, reverse=True)
    hlist=[]
    for k in brndcats:
          if k.phash not in hlist:
                 hlist.append(k.phash)
                 k.title=k.title[:20]+".."
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 if count>60:break
                 count=count+1
                 queryitems1[count%6].append(k)
                 #name=re.match(r'.*\.in/(.*)/dp/.*',k.amzlink).group(1)
                 #namelist.append("name")
    #queryitems1.sort(key=lambda x: x.dispscore, reverse=True)
    row1=queryitems1
    context = {
        
        'row': row1,
        'category': category,
        'catlst':catlstv,
        'travelp':11,
        }
    return render(request,'polls/colorbrand.html',context)

def findsimilar(request, category):
    queryitems=[]
    queryitems1=[[],[],[],[],[],[]]
    namelist=[]
    cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
    for i in cats:
        if(not i.tablename): continue
        brndcats=amznitems.objects.filter(brandcategory__icontains=i.tablename).all()
        count=0
        for k in brndcats:
            if k.amzimg not in imglst and k.blk==0:
                 imglst.append(k.amzimg)
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems.append(k)
                 name=re.match(r'.*\.in/(.*)/dp/.*',k.amzlink).group(1)
                 namelist.append(name)
    lt=len(queryitems)
    th=len(queryitems)/6
    count=0
    count1=0
    for i in queryitems[:60]:
        if count1>5:
            count1=0
        queryitems1[count1].append(i)
        count1=count1+1
    lt=len(queryitems)
    row1=queryitems1
    context = {

        'row': row1,
        'category': category,
        }
    return render(request,'polls/findsim.html',context)

def matchsimilar(request,onsource,pid,spid):
    if 'amazon' ==onsource:
        pdct=amznitems.objects.filter(id=pid).all()[0]
    elif onsource=='snapdeal':
        pdct=snapitems.objects.filter(id=pid).all()[0]
    elif onsource=='paytm':
        pdct=ptmitems.objects.filter(id=pid).all()[0]
    elif onsource=='infibeam':
        pdct=infiitems.objects.filter(id=pid).all()[0]
    else:
        pdct=flipitems.objects.filter(id=pid).all()[0]
    pdct.spid=spid
    pdct.save()
    context={'pid':pid,'spid':spid,}
    return render(request,'polls/matched.html',context) 
def blockthis(request,onsource,pid):
    if 'amazon' in onsource  :
       pdct=amznitems.objects.filter(id=pid).all()[0]
    else:
       pdct=flipitems.objects.filter(id=pid).all()[0]
    pdct.blk=1
    pdct.save()
    spid="blocked"
    context={'pid':pid,'spid':spid,}
    return render(request,'polls/matched.html',context)

def addtocat(request,onsource,pid,catval):
    if 'amazon' in onsource  :
       pdct=amznitems.objects.filter(id=pid).all()[0]
    else:
       pdct=flipitems.objects.filter(id=pid).all()[0]
    pdct.catval=catval
    pdct.save()
    spid="catagorised to "+ str(catval)
    context={'pid':pid,'spid':spid,}
    return render(request,'polls/matched.html',context)

def blockbrand(request,brand):
    pdct=amznitems.objects.filter(brandcategory__icontains=brand).all()
    for i in pdct:
       pdct.blk=2
       pdct.save()
    spid="blocked"
    context={'pid':brand,'spid':spid,}
    return render(request,'polls/matched.html',context)


def lsearch(request,searchquery):
    sq=searchquery.split()
    brndcats=amznitems.objects.filter().all() 
    poss_res=[]
    node_value=[]
    name=[]
    cnt=0
    for i in sq:
        for j in brndcats:
            if i in j.brandcategory:
               if j not in poss_res:
                   poss_res.append(j)
                   n1=j.amzlink
                   name.append(re.match(r'.*\.in/(.*)/dp.*',n1).group(1))
    context={'s_result':poss_res[:5],}
    return render(request,'polls/searchresult.html')
            
               
def loadmoretour(request, category,block):
    queryitems=[]
    namelist=[]
    cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
    for i in cats:
        if(not i.tablename): continue
        brndcats=amznitems.objects.filter(brandcategory__icontains=i.tablename).all()
        count=0
        for k in brndcats:
            if k.amzimg not in imglst:
                 imglst.append(k.amzimg)
                 k.amzimg=k.amzimg.replace('SL160','SL60')
                 queryitems.append(k)
                 name=re.match(r'.*\.in/(.*)/dp/.*',k.amzlink).group(1)
                 namelist.append(name)
    lt=len(queryitems)
    if block==1:
       row11=queryitems[:lt/2]
    else: row11=queryitems[lt/2:]
    if lt/2<200:
          row1=row11[100:lt/2]
    else: row1=row11[100:200]

    context = {
          'row1': row1,
          'category':category,
          'block':block,    
        }
#    return HttpResponse("doandfafa adf")
    return render(request,'polls/loadmoretour.html',context)

def loadmoreall(request, category,pgn,col):
    queryitems=[]
    namelist=[]
    queryitems1=[[],[],[],[],[],[]]
    q=category.replace(" ","_")
    brndcats=amznitems.objects.filter(brandcategory__icontains=q).order_by('-dispscore').all()
    count=0
    pgn=int(pgn)
    for k in brndcats:
                 if count>60*(pgn-1) :
                     k.title=k.title[:20]+".."
                     k.amzimg=k.amzimg.replace('SL160','SL260')
                     queryitems1[count%6].append(k)
                 if  count>60*pgn:
                      break
                 count=count+1
       #          name=re.match(r'.*\.in/(.*)/dp/.*',k.amzlink).group(1)
        #         namelist.append(name)
    context = {
          'row': queryitems1[int(col)],
        }
    return render(request,'polls/loadmoreall.html',context)

def mloadmoreall(request, category,pgn,col):
    queryitems=[]
    namelist=[]
    queryitems1=[[],[],[],[],[],[]]
    cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
    for i in cats:
        if(not i.tablename): continue
        brndcats=amznitems.objects.filter(brandcategory__icontains=i.tablename).all()
        count=0
        for k in brndcats:
            if k.amzimg not in imglst:
                 k.title=k.title[:20]+".."
                 imglst.append(k.amzimg)
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems.append(k)
                 name=re.match(r'.*\.in/(.*)/dp/.*',k.amzlink).group(1)
                 namelist.append(name)
    lt=len(queryitems)
    row11=[]
    pgn1=int(pgn)
    hl=(pgn1)*60
    ll=60*(pgn1-1)
    if(hl>lt):
        row11=queryitems[ll:lt]
    else:
        row11=queryitems[ll:hl]
    count=0
    count1=0
    for i in row11:
        if count1>5:
            count1=0
        queryitems1[count1].append(i)
        count1=count1+1
    row=queryitems1[int(col)]
    context = {
          'row': row,
        }
    return render(request,'polls/mlall.html',context)
    #return render(request,'polls/loadmoreall.html',context)
       

    
def retcategory(request, qid,category):
    queryitems=[]
    namelist=[]
    cats=amzntables.objects.filter(bagt__icontains=category).all()[:6]
    imglst=[]
    for i in cats:
        brndcats=amznitems.objects.filter(brandcategory__icontains=i.tablename).all()
        count=0
        for k in brndcats:
            if k.amzimg not in imglst:
                 imglst.append(k.amzimg)
                 queryitems.append(k)
                 name=re.match(r'.*\.in/(.*)/dp/.*',k.amzlink).group(1)
                 namelist.append(name)
    context = {
        'row': queryitems,
        }
    
#    return HttpResponse("doandfafa adf")
    return render(request,'polls/index4.html',context)
    

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
