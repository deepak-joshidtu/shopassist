
import MySQLdb
from polls.models import flipitems
import re
from polls.models import fltables
db = MySQLdb.connect("103.50.160.63","hotbuy5g_joshi","joshi123","hotbuy5g_prdctlist" )
cursor = db.cursor()

bagtypes=['Laptop backs','rucksacks','school bags','cabin luggage','travel duffles','travel accessories','briefcases','wallet for men','handbags','slingbags','wallet for women']
for ij in bagtypes:
    cursor.execute("select tablenames from "+ij.replace(" ","_"))
    bs=cursor.fetchall()
    for j in bs:
        cursor.execute(" SELECT count(*) FROM information_schema.TABLES WHERE  (TABLE_NAME = 'fl"+j[0]+"')")
        dropa=cursor.fetchall()
        if int(dropa[0][0])!=1:
                 continue
        if len(j)<1:
           continue
        cursor.execute("select * from fl" + j[0])
        fltables(bagt=ij,tablename="fl"+j[0]).save()
        brnds=cursor.fetchall()
        for i in brnds:
              try:  flipitems(brandcategory=j[0],amzlink=i[1],amzimg=i[2],price=i[3],brand=re.sub('[^a-zA-Z \.]+', '',i[4]),color=i[5],title=i[6],productid=i[7],sizev=i[8],colorv=i[9],features=i[10],spid=" ",blk=0,osource="flipkart").save()
              except IndexError,UnicodeDecodeError:
                    print "haha index"
  
 
