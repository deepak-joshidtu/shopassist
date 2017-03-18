import MySQLdb
from polls.models import amznitems
import re
from polls.models import amzntables
db = MySQLdb.connect("103.50.160.63","hotbuy5g_joshi","joshi123","hotbuy5g_prdctlist" )
cursor = db.cursor()

bagtypes=['Laptop bags']
for ij in bagtypes:
    cursor.execute("select tablenames from "+ij.replace(" ","_"))
    bs=cursor.fetchall()
    for j in bs:
        cursor.execute("select * from " + j[0])
        brnds=cursor.fetchall()
        cursor.execute("select * from fl" + j[0])
        brnds1=cursor.fetchall()
        
              
