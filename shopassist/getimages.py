
from lxml import etree
import xml.etree.ElementTree as ET
import MySQLdb
import os
from subprocess import call
ns={"atom":"http://www.flipkart.com/affiliate"}
db = MySQLdb.connect("103.50.160.63","hotbuy5g_joshi","joshi123","hotbuy5g_prdctlist" )
#db1 = MySQLdb.connect("localhost","root","joshi123","mysql" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
#cursor1=db1.cursor()
#cursor.execute("drop table fliplinks")
#cursor.execute("Create table fliplinks(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,fliplink VARCHAR(300) NOT NULL,flipimg VARCHAR(200) NOT NULL,price INT, brand varchar(30),color varchar(30))")
cursor.execute("select amzimg from amznlinks")
bs=cursor.fetchall()
cnt=1
for i in bs:
   call(['curl',i[0],'-o',str(cnt)+'.png'])
   cnt=cnt+1
