from polls.models import amznitems,amznitems1,amzntables
a=amzntables.objects.filter(bagt__icontains='messenger').all()
import re
for i in a:
    fst=0
    count=0
    b=amznitems.objects.filter(brandcategory__icontains=i.tablename).all()
    print i.bagt
    for j in b:
        if fst==0:
           if len(j.amzimg)<5:continue
           fst=1
           i.pid=j.id
           i.amzimg=j.amzimg
           i.brand=re.match(i.bagt.replace(" ","_")+'(.*)',i.tablename).group(1)
        count=count+1
    i.brandcount=count
    i.save()

       
   