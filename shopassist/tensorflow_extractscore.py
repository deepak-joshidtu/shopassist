import re
import os
f1=open('filenames','r')
count=0
f3=open("tempalltypes",'w')
for j in f1:
 if j[:-1].strip():
   f=open(j[:-1],'r')
   st=""
   count=count+1
   for i in f:
     b=re.match(r'.*/label_image/main.cc:206] (.*)',i)
     if b:
       st1=b.group(1)
   
       c=re.match(r'(catval[0-9]*) \([0-9]*\)\: ([0-9\.]*)',st1)
       if c:
          f3.write(j[:-1]+",,")
     




import re
import os
f1=open('filenames','r')
count=0
f3=open("flrmalltypes",'w')
for j in f1:
 if j[:-1].strip():
   f=open(j[:-1],'r')
   f2=open("flrmclasses/"+j[:-1],'w')
   f3.write(j[:-1]+": ")
   st=""
   count=count+1
   for i in f:
     b=re.match(r'.*/label_image/main.cc:206] (.*)',i)
     if b:
       st1=b.group(1)
   
       c=re.match(r'(catval[0-9]*) \([0-9]*\)\: ([0-9\.]*)',st1)
       if c:
         st+=c.group(1)+","+c.group(2)+","
      # print c.group(1)
       #if os.path.isfile("../../images2/images/"+j[:-1]):
        #os.rename("../../images2/images/"+j[:-1],"../../images2/images"+c.group(1)+str(count))
        #print c.group(1)
   f3.write(st+"\n")
   f2.write(st)
   f2.close()
        


   
a="catval10 (5): 0.595617,catval2 (12): 0.0636281,catval15 (2): 0.050981,catval16 (0): 0.0503123,catval4 (7): 0.0453865,"
b=a.split(",")
for i in b:
   c=re.match(r'(catval[0-9]*) \([0-9]*\)\: ([0-9\.]*)',i)
   if c:
     print c.group(1)
     print c.group(2)


db.polls_amznitems.find().forEach(function(d){ db.getSiblingDB('test')['polls_amznitems'].insert(d); });

