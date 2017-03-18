from django.http import HttpResponse
from .models import myCollection3
from polls.models import flipitems
from django.template import loader
from django.shortcuts import render
from .models import amznitems
from .models import amzntables
from .models import colorcounts
from .models import brandcounts
from difflib import SequenceMatcher as SM
import re
def index(request):
    cate=['messenger bags','Laptop bags','rucksacks','school bags','cabin luggage','check in luggage','travel duffles','travel accessories','briefcases','wallet for men','handbags','slingbags']
    cateimgs=['http://ecx.images-amazon.com/images/I/41XdPx32kvL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/413Ahn89wrL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/51Yg7PAmK0L._AC_UL246_SR190,246_.jpg' ,'http://ecx.images-amazon.com/images/I/41ug3NXVvqL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41HPNlWFkdL._AC_UL246_SR190,246_.jpg' ,
'http://ecx.images-amazon.com/images/I/41Lff8oitLL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41iDncnPOyL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41vGGhKQiwL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/51vnaQ2JGoL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/41nnRhGmCYL._AC_UL246_SR190,246_.jpg','http://ecx.images-amazon.com/images/I/417PsjAihZL._AC_UL260_SR200,260_.jpg','http://ecx.images-amazon.com/images/I/41ReiAOMZ1L._AC_UL260_SR200,260_.jpg']
    count=0
    cate1=[]
    cate2={'cate1':'','cate2':'','cateimgs':'','cateimgs1':''}
    cateimgs1=[]
    cateimgs2=[]
    for i in cate:
        if count%2==0:
            cate2={'cate1':i,'cate2':cate[count+1],'cateimg1':cateimgs[count],'cateimg2':cateimgs[count+1]}
            cate1.append(cate2)
        count=count+1
    context={'category':cate1,}
    return render(request, 'polls/home1.html',context)

def blog(request):
     return render(request,'polls/blog.html')
def productdetail(request,pdctid):
    
    pdct=amznitems.objects.filter(id=pdctid).all()[0]
    pdctsame=amznitems.objects.filter(spid=pdctid).all()
    n1=pdct.amzlink
    name=re.match(r'.*\.in/(.*)/dp.*',n1).group(1)
    imgs=[]
    if(len(pdct.amzimg0)>4):imgs.append(pdct.amzimg0)
    if(len(pdct.amzimg1) >4):imgs.append(pdct.amzimg1)
    if(len(pdct.amzimg2)>4):imgs.append(pdct.amzimg2)
    if(len(pdct.amzimg3)>4):imgs.append(pdct.amzimg3)
    if(len(pdct.amzimg4)>4):imgs.append(pdct.amzimg4)
    sgrp=[]
    if pdct.pdgrp >0:
       grp=amznitems.objects.filter(pdgrp=pdct.pdgrp).all()
       for i in grp:
         if i.id not in pdct.id:
              sgrp.append(i)
    context = {
        'pdct': pdct,
        'name':name,
        'imgs':imgs,
         'pdctsame':pdctsame,
        'sgrp':sgrp,
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
    brndcats=amznitems.objects.filter(brandcategory__icontains=category.replace(" ","_")).all()
    for k in brndcats:
            if k.amzimg not in imglst:
                 imglst.append(k.amzimg)
                 if k.color not in colorlst:
                       colit=colorcounts.objects.filter(colorcategory__icontains=category.replace(" ","_")+k.color).all()
                       if colit:
                           colitems.append(colit[0].colorcount)
                           colorlst.append(k.color)
                           k.amzimg=k.amzimg.replace('SL160','SL260')
                           queryitems.append(k)
                        
    th=len(queryitems)/6
    count=0
    count1=0
    for i in queryitems:
        if count1>5:
            count1=0
        wrapper[count1].append({'row':i,'nitems':colitems[count]})
        queryitems1[count1].append(i)
        count1=count1+1
        count=count+1

    lt=len(queryitems)
    row1=queryitems1
    context = {
        
        'row': wrapper,
        'category': category,
        }

    return render(request, 'polls/thome5.html',context)

def catecolor(request,category,color):
    allcolors=['red','blue','green','purple','orange','grey','black']
    queryitems1=[[],[],[],[],[],[]]
    queryitems=[]
    namelist=[]
    imglst=[]
    colorlst=[]
    count=0
    count1=0
    colorn="lightgrey"
    for i in allcolors:
        if i[1:] in color:
           colorn=i
           break
    brndcats=amznitems.objects.filter(brandcategory__icontains=category.replace(" ","_"),color=color).all()
    for k in brndcats:
            if k.amzimg not in imglst:
                       imglst.append(k.amzimg)
              #   if color in k.color or k.color in color:
#                       colorlst.append(k.color)
                       count=count+1
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
        'color': color,
        'colorn':colorn,
        }
  

    return render(request, 'polls/coloritems.html',context)

def catebrand(request,category,brand):
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
        if k.amzimg not in imglst :#and k.blk==0:# and k.spid not in lid  :
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
        if k.amzimg not in imglst:# and k.blk==0:# and k.spid not in lid  :
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
    for i in cats:
        if(not i.tablename): continue
        if count>th:
             count=0
             count1=count1+1
        brndcats=amznitems.objects.filter(brandcategory__icontains=i.tablename).all()
        for k in brndcats:
            if k.amzimg not in imglst:
                 imglst.append(k.amzimg)
                 if brand in k.brand or k.brand in brand:
#                      colorlst.append(k.color)
                       count=count+1
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
    metab1=" "
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
    metab1=" "
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
    brndcats=amznitems.objects.filter(brandcategory__icontains=category.replace(" ","_"),price__gte=p1,price__lte=p2).all()
    for k in brndcats:
        #    k=brndcats[0]
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
    metab1=" "
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

    return render(request, 'polls/byprice.html',context)



def tbrand1(request,category):
    queryitems1=[[],[],[],[],[],[]]
    queryitems=[]
    namelst=[]
    cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
    count=0
    count1=0
    brnd=[]
    wrapper=[[],[],[],[],[],[]]
    th=len(cats)/6
    for i in cats:
        if(not i.tablename): continue
        if count>th:
           count=0
           count1=count1+1
        brndcats=amznitems.objects.filter(brandcategory__icontains=i.tablename).order_by('brand').all()
        for k in brndcats:
          if k.brand.strip():
           if SM(None,k.brandcategory.replace(category.replace(" ","_"),""),k.brand).ratio()>0.8:
            if k.amzimg not in imglst:
                 brnd.append(k.brand)
                 imglst.append(k.amzimg)
                 k.amzimg=k.amzimg.replace('SL160','SL260')
                 queryitems.append(k)
                 count=count+1
                 name=" "
                 if re.match(category.replace(" ","_")+'(.*)',k.brandcategory):
                     name=re.match(category.replace(" ","_")+'(.*)',k.brandcategory).group(1)
                 namelst.append(name)
                 break
    th=len(queryitems)/6
    count=0
    count1=0
    for i in queryitems:
        if count1>5:
            count1=0
        ak=brandcounts.objects.filter(brandcategory__icontains=i.brandcategory).all()
        if ak:
          wrapper[count1].append({'row':i,'brandcount':ak[0].brandcount})
          queryitems1[count1].append(i)
          count1=count1+1
    cnt=0
    metab1=" "
    for i in brnd:
       if cnt>4:break
       cnt=cnt+1
       metab1=metab1+", "+i
    lt=len(queryitems)
    row1=queryitems1

    context = {
        'metab1':metab1,
        'row': wrapper,
         'category': category,
        'name':namelst,
        }

    return render(request, 'polls/thome4.html',context)

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

def tours(request, category):
    queryitems=[]
    queryitems1=[[],[],[],[],[],[]]
    namelist=[]
    #cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
   # for i in cats:
   #     if(not i.tablename): continue
    brndcats=amznitems.objects.filter(brandcategory__icontains=category.replace(" ","_")).order_by('dispscore').all()
    count=0
    for k in brndcats:
            if k.amzimg not in imglst and k.blk==0 :
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
    cats=amzntables.objects.filter(bagt__icontains=category).all()
    imglst=[]
    for i in cats:
        if(not i.tablename): continue
        brndcats=amznitems.objects.filter(brandcategory__icontains=i.tablename).all()
        count=0
        for k in brndcats:
            if k.amzimg not in imglst:
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
