from time import strftime, gmtime, sleep
from lxml import etree
import xml.etree.ElementTree as ET
import MySQLdb
import os
import re
from subprocess import call
ns={"atom":"http://www.flipkart.com/affiliate"}
db = MySQLdb.connect("103.50.160.63","hotbuy5g_joshi","joshi123","hotbuy5g_prdctlist" )
db1 = MySQLdb.connect("localhost","root","joshi123","mysql" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
cursor1=db1.cursor()
#cursor.execute("drop table fliplinks")
#cate=['Laptop bags','rucksacks','school bags','cabin luggage','check in luggage','travel duffles','travel accessories','briefcases','wallet for men','handbags','slingbags']
cate=['Laptop backpacks']
for i in cate:
#        cursor.execute("select tablenames from "+ i.replace(" ","_"))
 #       tables=cursor.fetchall()
        tables=[]
        ques=[]
        fbr=open('laptop_backpacks_brand','r')
        for ibr in fbr:
              b=re.match(r' *([a-zA-z ]*) *\(([0-9]*)\) *',ibr)
              if b:
                   tables.append(b.group(1)[:-1])
        for ij1 in tables:
             ij=i.replace(" ","_")+ij1
             ij=ij.replace(" ","")
             cursor.execute(" SELECT count(*) FROM information_schema.TABLES WHERE  (TABLE_NAME = 'fl"+ij+"')")
             dropa=cursor.fetchall()
             if int(dropa[0][0])==1:
                 cursor.execute("drop table fl"+ij )
             cursor.execute("Create table fl"+ij+"(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,amzlink VARCHAR(300) NOT NULL,amzimg VARCHAR(200) NOT NULL,price INT, brand varchar(30),color varchar(30),title varchar(30),productid varchar(50),sizev varchar(50),colorv varchar(50),features varchar(3000))")
             qs=ij.replace(i.replace(" ","_"),"")
             ques.append(i+" "+qs)
             bcnt=1;
             bkw=ij1+" "+i#qs+" "+i
             bkw=bkw.replace(" ","+")
             if not os.path.isfile(ij):
                sleep(1.3)
                call(['curl','-H','Fk-Affiliate-Id:myselfdjo','-H','Fk-Affiliate-Token:29f4e86c5a9a42d4ba9caf49052fabaa','https://affiliate-api.flipkart.net/affiliate/search/xml?query='+bkw+'&resultCount=10','-o',ij])
                print    'https://affiliate-api.flipkart.net/affiliate/search/xml?query='+bkw+'&resultCount=10'
             if os.path.isfile(ij):
                 kit=etree.parse(ij)
                 items=kit.xpath('//productAttributes', namespaces=ns)
                 for k in items:
                     if k.xpath('.//productUrl/text()'):
                        t2=k.xpath('.//productUrl/text()')[0]
                     else: t2=" "
                     print t2
                     if k.xpath('./imageUrls//value/text()'):
                        t1=k.xpath('./imageUrls//value/text()')[0]
                     else: t1=" "
                     print t1
                     if k.xpath('.//sellingPrice/amount/text()'):
                           prc=k.xpath('.//sellingPrice/amount/text()')[0]
                     else:
                         prc="0"
                     print prc
                     if k.xpath('.//color/text()'):
                         colr=k.xpath('.//sellingPrice/amount/text()')[0]
                     else:
                         colr=" "
                     if(k.xpath('.//productBrand/text()', namespaces=ns)):
                         brand=k.xpath('.//productBrand/text()', namespaces=ns)[0] 
                     else:
                         brand=" "
                     brand=re.sub('[^a-zA-Z \.]+', '',brand)   
                     print brand  
                     if(k.xpath('.//title/text()', namespaces=ns)):
                         title=k.xpath('.//title/text()', namespaces=ns)[0] 
                     else:
                         title=" "   
                     title=re.sub('[^a-zA-Z \.]+', '',title)
                     print title
                     if(k.xpath('.//sizeVariants/text()', namespaces=ns)):
                         sizevar=k.xpath('.//sizeVariants/text()', namespaces=ns)[0] 
                     else:
                         sizevar=" "   
                     print sizevar
                     if(k.xpath('.//colorVariants/text()', namespaces=ns)):
                         colorvar=k.xpath('.//colorVariants/text()', namespaces=ns)[0] 
                     else:
                         colorvar=" "   
                     print colorvar    
                     if(k.xpath('.//productDescription/text()', namespaces=ns)):
                         productDes=k.xpath('.//productDescription/text()', namespaces=ns)[0] 
                     else:
                         productDes=" "
                     print "adf"+productDes+"adf"
                     if productDes:  
                        productDes=re.sub('[^a-zA-Z0-9\. ]+', '',productDes) 
                     print "adf"+productDes+"adf"
                     if(k.xpath('//productId/text()', namespaces=ns)):
                         productId=k.xpath('//productId/text()', namespaces=ns)[0] 
                     else:
                         productId=" "   
                     print productId            
                     cursor.execute("Insert into fl"+ij+"(amzlink, amzimg,price,brand,color,title,productid,sizev,colorv,features) VALUES ('"+ t2+"', '"+ t1+"', "+ prc+",'"+ brand+"','"+colr+"','"+title+"','"+productId+"','"+sizevar+"','"+colorvar+"','"+productDes+"')")
  



            
             
            
