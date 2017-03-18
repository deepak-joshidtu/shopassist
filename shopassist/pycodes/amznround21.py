from base64 import b64encode
from datetime import datetime, timedelta
import functools
from hashlib import sha256
import hmac
import socket
import sys
from time import strftime, gmtime, sleep
import warnings
import re
import six
from lxml import etree
import xml.etree.ElementTree as ET
import MySQLdb
import time
import os.path
try:
    from io import StringIO
    from urllib.request import HTTPError
    from urllib.parse import quote
except ImportError:
    from cStringIO import StringIO
    from urllib2 import HTTPError
    from urllib2 import quote

import requests
db = MySQLdb.connect("103.50.160.63","hotbuy5g_joshi","joshi123","hotbuy5g_prdctlist" )
db1 = MySQLdb.connect("localhost","root","joshi123","mysql" )
# prepare a cursor object using cursor() method
cursor = db.cursor()

#cursor.execute("drop table amznlinks")
#cursor.execute("Create table amznlinks(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,amzlink VARCHAR(200) NOT NULL,amzimg VARCHAR(200) NOT NULL)")

errf1=open("errorfiles1",'w')
errf2=open("errorfiles2",'w')
keyword=" "
itempage=2

ns={"atom":"http://webservices.amazon.com/AWSECommerceService/2013-08-01"}
fnms=open('filenames','r')
fnl=[]
for i in fnms:
    if i[:-2] not in fnl:
         fnl.append(i[:-2])

# prepare a cursor object using cursor() method
#cursor = db.cursor()
#cursor.execute("drop table amznlinks")
#cursor.execute("Create table amznlinkstmp(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,amzlink VARCHAR(300) NOT NULL,amzimg VARCHAR(200) NOT NULL,price INT, brand varchar(30),color varchar(20),height int,width int,length int,weight int,offerprice int)")
#cursor.execute("Create table amznlinks(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,amzlink VARCHAR(300) NOT NULL,amzimg VARCHAR(200) NOT NULL,price INT, brand varchar(30),color varchar(20),height int,width int,length int,weight int,offerprice int)")
def _build_url2(self,**qargs):
        items=0
        # remove empty (=None) parameters
        for key in list(qargs):
            if qargs[key] is None:
                del qargs[key]
        if 'AWSAccessKeyId' not in qargs:
            qargs['AWSAccessKeyId'] = "AKIAIONPSL3ZZWB6AW7Q"
        if 'Service' not in qargs:
            qargs['Service'] = 'AWSECommerceService'
        # use the version this class was build for by default
        if 'Version' not in qargs:
            qargs['Version'] = "2013-08-01"
        if 'AssociateTag' not in qargs :
            qargs['AssociateTag'] = "buybest01-21"
        #if isinstance(qargs.get('ResponseGroup'), list):
        qargs['ResponseGroup'] = "ItemAttributes,Images,OfferSummary"
        global keyword      
        qargs['Operation']="ItemSearch"
        qargs['SearchIndex']="Luggage"
        #global itempage
        #itempage=itempage+2
        #quargs['ItemPage']=str(itempage)
        qargs['ItemPage']="2"
        # add timestamp (this is required when using a signature)
        qargs['Timestamp'] = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
        # create signat  
        fnd=0
        bagtypes=['Laptop bags','rucksacks','school bags','cabin luggage','travel duffles','travel accessories']#,'messenger bags','briefcases','wallet for men','wallet for women','handbags','slingbags','tote bags','check in luggage']
        for bagt in bagtypes:
            baz=[]
            cursor.execute(" SELECT count(*) FROM information_schema.TABLES WHERE  (TABLE_NAME = '"+bagt.replace(" ","_")+"')")
            dropa=cursor.fetchall()
            if int(dropa[0][0])==1:
                 cursor.execute("drop table "+bagt.replace(" ","_") )
            print  bagt.replace(" ","_") 
            cursor.execute("Create table "+bagt.replace(" ","_")+"(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,tablenames VARCHAR(30) NOT NULL)")
            qargs['Timestamp'] = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
            qargs['ResponseGroup'] = "ItemAttributes"
            qargs['Keywords']=bagt
            for pgs in range(1,10):
               qargs['ItemPage']=str(pgs)
               keys = sorted(qargs.keys())
               args = '&'.join('%s=%s' % (
                key, quote(str(qargs[key]).encode('utf-8'))) for key in keys)
               msg = 'GET'
               msg += '\nwebservices.amazon.in' 
               msg += '\n/onca/xml'
               msg += '\n' + args
               key = "fGIE0vmLiBqnvGYJ/NKJNMj9nM4qgEIHGlBjoc6B" or ''
        # On python3, HMAC needs bytes for key and msg.
               try:
                   hash = hmac.new(key, msg, sha256)
               except TypeError:
                 hash = hmac.new(key.encode(), msg.encode(), sha256)
               signature = quote(b64encode(hash.digest()))
               url= 'http://%s/onca/xml?%s&Signature=%s' % (
                "webservices.amazon.in", args, signature)      
               print url
               sleep(1.3)
               if(not(os.path.isfile(bagt+str(pgs)))):
                   response1 = requests.get(url, stream=True)
                   fxm =open(bagt+str(pgs),'w')
                   fxm.write(response1.text.encode('utf-8'))
                   fxm.close()
               kit=etree.parse(bagt+str(pgs))
               if(kit.xpath('//atom:TotalPages/text()', namespaces=ns)):
                   tpgs=int(kit.xpath('//atom:TotalPages/text()', namespaces=ns)[0])
               if(kit.xpath('//atom:TotalPages/text()', namespaces=ns)):
                      if pgs>tpgs:
                           errf0.write(bagt+"\n")
                           break
               else: break
               items=kit.xpath('//atom:Item', namespaces=ns)
               for k in items:
                 if(k.xpath('.//atom:Brand/text()', namespaces=ns)):
                     brand=k.xpath('.//atom:Brand/text()', namespaces=ns)[0] 
                 else:
                     brand=" "
                 if brand.replace("'","") not in baz:
                       brand=brand.replace(" ","")
                       brand=brand.replace("-","")
                       brand=re.sub('[^a-zA-Z]+', '',brand)
                       brand=brand.encode('utf-8')
                       baz.append(brand.replace("'",""))
                       
                       print brand
                       cursor.execute("insert into "+bagt.replace(" ","_")+"(tablenames) values (\""+bagt.replace(" ","_")+brand.replace("'","")+"\")")      
            for subbrnd in baz:
             print subbrnd
             if subbrnd.strip():
              cursor.execute(" SELECT count(*) FROM information_schema.TABLES WHERE  (TABLE_NAME = '"+bagt.replace(" ","_")+subbrnd+"')")
              dropa=cursor.fetchall()
              if int(dropa[0][0])==1:
                 cursor.execute("drop table "+bagt.replace(" ","_")+ subbrnd )
              print subbrnd
              if (not subbrnd):
                  continue                 
              cursor.execute("Create table `"+bagt.replace(" ","_")+subbrnd+"`(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,amzlink VARCHAR(300) NOT NULL,itemlink1 VARCHAR(300),itemlink2 VARCHAR(300),itemlink3 VARCHAR(300),itemlink4 varchar(300),amzimg VARCHAR(300) NOT NULL,amzimg0 VARCHAR(200),amzimg1 VARCHAR(200),amzimg2 VARCHAR(200),amzimg3 VARCHAR(200),amzimg4 VARCHAR(200),amzimg5 VARCHAR(200),price INT, brand varchar(30),color varchar(20),binding varchar(20),department varchar(20),features VARCHAR(2000),productgroup varchar(30),size varchar(30),title varchar(30),height int,width int,length int,weight int,offerprice int,salesrank int,sim0 varchar(50),sim1 varchar(50),sim2 varchar(50),sim3 varchar(50),sim4 varchar(50),asin varchar(50))")
            #  cursor.execute("Create table amznlinks(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,amzlink VARCHAR(300) NOT NULL,itemlink1 VARCHAR(300),itemlink2 VARCHAR(300),itemlink3 VARCHAR(300),itemlink4 varchar(300),amzimg VARCHAR(300) NOT NULL,amzimg0 VARCHAR(200),amzimg1 VARCHAR(200),amzimg2 VARCHAR(200),amzimg3 VARCHAR(200),amzimg4 VARCHAR(200),amzimg5 VARCHAR(200),price INT, brand varchar(30),color varchar(20),binding varchar(20),department varchar(20),features VARCHAR(2000),productgroup varchar(30),size varchar(30),title varchar(30),height int,width int,length int,weight int,offerprice int)")        
              qargs['Keywords']=subbrnd+" "+bagt
              qargs['Timestamp'] = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
              qargs['ResponseGroup'] = "ItemAttributes,Images,OfferSummary,SalesRank,Similarities"
              for pgs in range(1,5):
               qargs['ItemPage']=str(pgs)
               keys = sorted(qargs.keys())
               args = '&'.join('%s=%s' % (
                key, quote(str(qargs[key]).encode('utf-8'))) for key in keys)
               msg = 'GET'
               msg += '\nwebservices.amazon.in' 
               msg += '\n/onca/xml'
               msg += '\n' + args
               key = "fGIE0vmLiBqnvGYJ/NKJNMj9nM4qgEIHGlBjoc6B" or ''
        # On python3, HMAC needs bytes for key and msg.
               try:
                   hash = hmac.new(key, msg, sha256)
               except TypeError:
                 hash = hmac.new(key.encode(), msg.encode(), sha256)
               signature = quote(b64encode(hash.digest()))
               url= 'http://%s/onca/xml?%s&Signature=%s' % (
                "webservices.amazon.in", args, signature)      
               print url
               sleep(1.3)
               if(not(os.path.isfile(bagt+subbrnd+str(pgs)))):
                   response1 = requests.get(url, stream=True)
                   fxm =open(bagt+subbrnd+str(pgs),'w')
                   fxm.write(response1.text.encode('utf-8'))
                   fxm.close()
               kit=etree.parse(bagt+subbrnd+str(pgs))
               if(kit.xpath('//atom:TotalPages/text()', namespaces=ns)):
                   tpgs=int(kit.xpath('//atom:TotalPages/text()', namespaces=ns)[0])
               if(kit.xpath('//atom:TotalPages/text()', namespaces=ns)):
                      if pgs>tpgs:
                           errf1.write(bagt+subbrnd+"\n")
                           break
               else: break
               items=kit.xpath('//atom:Item', namespaces=ns)
               for k in items:
                 print pgs
                 if k.xpath('./atom:ASIN/text()', namespaces=ns):
                    asin=k.xpath('./atom:ASIN/text()', namespaces=ns)[0]
                 else:
                    asin=" "
                 print asin
                 if(k.xpath('.//atom:SimilarProduct', namespaces=ns)):
                    simp=k.xpath('.//atom:SimilarProduct', namespaces=ns)
                    size=len(simp)
                    sim0=simp[0].xpath('./atom:ASIN/text()', namespaces=ns)[0]
                    if size>1:
                       sim1=simp[1].xpath('./atom:ASIN/text()', namespaces=ns)[0]
                    else:
                       sim1=" "
                    if size>2:
                       sim2=simp[2].xpath('./atom:ASIN/text()', namespaces=ns)[0]
                    else:
                       sim2=" "
                    if size>3:
                        sim3=simp[3].xpath('./atom:ASIN/text()', namespaces=ns)[0]
                    else:
                        sim3=" "
                    if size>4:
                        sim4=simp[4].xpath('./atom:ASIN/text()', namespaces=ns)[0]
                    else:
                        sim4=" "
                 else:
                     sim0=" "
                     sim1=" "
                     sim2=" "
                     sim3=" "
                     sim4=" "
                 print sim0
                 print "simi"
                 print sim1
                 print sim2
                 print sim3
                 if k.xpath('.//atom:DetailPageURL/text()', namespaces=ns):
                    t2=k.xpath('.//atom:DetailPageURL/text()', namespaces=ns)[0]
                 else:
                    t2=" "
                 print t2
                 if(k.xpath('.//atom:ItemLinks//atom:URL/text()', namespaces=ns)):
                    size=len(k.xpath('.//atom:ItemLinks//atom:URL/text()', namespaces=ns))
                    itml1=k.xpath('.//atom:ItemLinks//atom:URL/text()', namespaces=ns)[0]
                    if size>1:
                       itml2=k.xpath('.//atom:ItemLinks//atom:URL/text()', namespaces=ns)[1]
                    else:
                       itml2=" "
                    if size>2:
                       itml3=k.xpath('.//atom:ItemLinks//atom:URL/text()', namespaces=ns)[2]
                    else:
                       itml3=" "
                    if size>3:
                        itml4=k.xpath('.//atom:ItemLinks//atom:URL/text()', namespaces=ns)[3]
                    else:
                        itml4=" "
                 if k.xpath('./atom:MediumImage/atom:URL/text()', namespaces=ns):
                    t1=k.xpath('./atom:MediumImage/atom:URL/text()', namespaces=ns)[0]
                 else:
                    t1=" "
                 print t1
                 if k.xpath('./atom:SalesRank/text()', namespaces=ns):
                    salesrank=k.xpath('./atom:SalesRank/text()', namespaces=ns)[0]
                 else:
                    salesrank=str(10000)
                 print "salesrankd"+salesrank
                 if(k.xpath('./atom:ImageSets//atom:MediumImage/atom:URL/text()', namespaces=ns)):
                     size=len(k.xpath('./atom:ImageSets//atom:MediumImage/atom:URL/text()', namespaces=ns))
                     img0=k.xpath('./atom:ImageSets//atom:MediumImage/atom:URL/text()', namespaces=ns)[0]
                     if size>1:
                         imgl1=k.xpath('./atom:ImageSets//atom:MediumImage/atom:URL/text()', namespaces=ns)[1]
                     else: imgl1=" "
                     if size>2:
                         imgl2=k.xpath('./atom:ImageSets//atom:MediumImage/atom:URL/text()', namespaces=ns)[2]
                     else: imgl2=" "
                     if size>3:
                        imgl3=k.xpath('./atom:ImageSets//atom:MediumImage/atom:URL/text()', namespaces=ns)[3]
                     else: imgl3=" "
                     if size>4:
                        imgl4=k.xpath('./atom:ImageSets//atom:MediumImage/atom:URL/text()', namespaces=ns)[4]
                     else: imgl4=" "
                     if size>5:
                        imgl5=k.xpath('./atom:ImageSets//atom:MediumImage/atom:URL/text()', namespaces=ns)[5]
                     else: imgl5=" "
                 if k.xpath('//atom:LowestNewPrice/atom:Amount/text()', namespaces=ns):
                     offerprice=k.xpath('//atom:LowestNewPrice/atom:Amount/text()',namespaces=ns)[0]
                 else:
                    offerprice="0"
                 print offerprice
                 if k.xpath('.//atom:Amount/text()', namespaces=ns):
                    prc=k.xpath('.//atom:Amount/text()', namespaces=ns)[0]
                 else:
                     prc="0"
                 print prc
                 if k.xpath('.//atom:Binding/text()', namespaces=ns):
                    binding=k.xpath('.//atom:Binding/text()', namespaces=ns)[0]
                 else:
                    binding=" "
                 if k.xpath('.//atom:Department/text()', namespaces=ns):
                      department=k.xpath('.//atom:Department/text()', namespaces=ns)[0]
                 else:
                    department=" "
                 features=" "
                 if k.xpath('.//atom:Feature/text()', namespaces=ns):
                     for i in k.xpath('.//atom:Feature/text()', namespaces=ns):
                        features=features+i+". "  
                     features=re.sub('[^a-zA-Z0-9\. ]+', '',features)                                         
                 print prc             
                 if(k.xpath('.//atom:ProductGroup/text()', namespaces=ns)):
                     productgroup=k.xpath('.//atom:ProductGroup/text()', namespaces=ns)[0] 
                 else:
                     productgroup=" "
                 if(k.xpath('.//atom:Size/text()', namespaces=ns)):
                     size=k.xpath('.//atom:Size/text()', namespaces=ns)[0] 
                 else:
                     size=" "
                 if(k.xpath('.//atom:Title/text()', namespaces=ns)):
                    title=k.xpath('.//atom:Title/text()', namespaces=ns)[0] 
                 else:
                     title=" "  
                 title=re.sub('[^a-zA-Z0-9\.]+', '',title)   
                 if(k.xpath('.//atom:Brand/text()', namespaces=ns)):
                     brand=k.xpath('.//atom:Brand/text()', namespaces=ns)[0] 
                 else:
                     brand=" "
                 brand
                 if(k.xpath('.//atom:Color/text()', namespaces=ns) ):
                    color=k.xpath('.//atom:Color/text()', namespaces=ns)[0]
                 else:
                   color=" "
                 if k.xpath('.//atom:PackageDimensions/atom:Height/text()', namespaces=ns):
                    height=k.xpath('.//atom:PackageDimensions/atom:Height/text()', namespaces=ns)[0] 
                    print  height
                 if k.xpath('.//atom:PackageDimensions/atom:Width/text()', namespaces=ns):
                    width=k.xpath('.//atom:PackageDimensions/atom:Width/text()', namespaces=ns)[0]  
                    print width
                 if k.xpath('.//atom:PackageDimensions/atom:Length/text()', namespaces=ns):
                    length=k.xpath('.//atom:PackageDimensions/atom:Length/text()', namespaces=ns)[0]
                    print length
                 if k.xpath('.//atom:PackageDimensions/atom:Weight/text()', namespaces=ns):
                    weight=k.xpath('.//atom:PackageDimensions/atom:Weight/text()', namespaces=ns)[0]
                    print weight
                 else:
                    height="0"
                    width="0"
                    length="0"
                    weight="0"
                 try: 
                      print "Insert into  `"+bagt.replace(" ","_")+subbrnd+"`(amzlink, amzimg,price,brand,color,height,width,length,weight,offerprice) VALUES ('"+ t2+"', '"+ t1+"', "+ prc+",'"+ brand.replace("'","")+"', '"+ str(color)+"', "+ height+", "+ width+", "+ length+", "+ weight+","+offerprice+")"
                      cursor.execute("Insert into  `"+bagt.replace(" ","_")+subbrnd+"`(amzlink,itemlink1,itemlink2,itemlink3,itemlink4, amzimg,amzimg0,amzimg1,amzimg2,amzimg3,amzimg4,amzimg5,price,brand,color,binding,department,features,productgroup,size,title,height,width,length,weight,offerprice,sim0,sim1,sim2,sim3,sim4,asin,salesrank) VALUES ('"+ t2+"', '"+itml1+"','"+itml2+"','"+itml3+"','"+itml4+"','"+ t1+"', '"+img0+"','"+imgl1+"','"+imgl2+"','"+imgl3+"','"+imgl4+"','"+imgl5+"',"+ prc+",'"+ re.sub('[^a-zA-Z \.]+', '',brand) +"', '"+ str(color)+"','"+binding+"','"+department+"','"+features+"','"+productgroup+"','"+size+"','"+title+"',"+ height+", "+ width+", "+ length+", "+ weight+","+offerprice+",'"+sim0+"','"+sim1+"','"+sim2+"','"+sim3+"','"+sim4+"','"+asin+"',"+salesrank+")")
                 except UnicodeEncodeError,cursor.ProgrammingError:
                      print "error at haha"

 
quotes=[]
url=_build_url2(quotes)



    
