
import MySQLdb
from polls.models import snapitems
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
       
        cursor.execute("select * from snapdealproducts where  id>26000 " )
       
        brnds=cursor.fetchall()
        for i in brnds:
               snapitems(brandcategory=" ",amzlink=i[1],list_url=i[2],amzimg=i[3]).save()
              
  
 
