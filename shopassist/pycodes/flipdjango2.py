
import MySQLdb
from polls.models import flipitems
import re
from polls.models import fltables
db = MySQLdb.connect("103.50.160.63","hotbuy5g_joshi","joshi123","hotbuy5g_prdctlist" )
cursor = db.cursor()

bagtypes=['Laptop backpacks','rucksacks','school bags','cabin luggage','travel duffles','travel accessories','briefcases','wallet for men','handbags','slingbags','wallet for women']
for bagt in bagtypes:
        baz=[]
        f=open("brands/"+bagt.replace(" ","_"),'r')
        for i in f:
              baz=i.split("|")  
        for subbrnd in baz:
             subbrnd=re.sub('[^a-zA-Z0-9 ]+', '',subbrnd)
             tabnam=bagt.replace(" ","_")+ subbrnd.replace(" ","")
             cursor.execute(" SELECT count(*) FROM information_schema.TABLES WHERE  (TABLE_NAME = 'fl"+tabnam+"')") 
             dropa=cursor.fetchall()
             if int(dropa[0][0])!=1:
                 continue  
             fltables(bagt=bagt,tablename="fl"+tabnam).save()
             cursor.execute("select * from fl" + tabnam)
             brnds=cursor.fetchall()
             for i in brnds:
                try:  flipitems(brandcategory=tabnam,amzlink=i[1],amzimg=i[2],price=i[3],brand=re.sub('[^a-zA-Z \.]+', '',i[4]),color=re.sub('[^a-zA-Z \.]+', '',i[5]),title=i[6],productid=i[7],sizev=i[8],colorv=i[9],features=i[10],spid=" ",blk=0,osource="flipkart").save()
                except IndexError,UnicodeDecodeError:
                    print "haha index"
  
 
