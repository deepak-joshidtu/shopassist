
import MySQLdb
from polls.models import ptmitems
import re
from polls.models import fltables
db = MySQLdb.connect("103.50.160.63","hotbuy5g_joshi","joshi123","hotbuy5g_prdctlist" )
cursor = db.cursor()

bagtypes=['Laptop bags','rucksacks','school bags','cabin luggage','check in luggage','travel duffles','travel accessories','briefcases','wallet for men','handbags','slingbags']
#for ij in bagtypes:
if 1:
    #cursor.execute("select tablenames from "+ij.replace(" ","_"))
    #bs=cursor.fetchall()
    #for j in bs:
       
        cursor.execute("select * from paytmproducts " )
       
        brnds=cursor.fetchall()
        for i in brnds:
              try:  ptmitems(brandcategory=" ",amzlink=i[1],amzimg=i[2],price=i[3],brand=i[4],title=re.sub('[^a-zA-Z0-9\. ]+', '',i[5])).save()
              except IndexError,UnicodeDecodeError:
                    print "haha index"
  
 
