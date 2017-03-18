from polls.models import amznitems,flipitems,ptmitems,snapitems,infiitems
a=amznitems.objects.filter().all()
maxv=0
for i in a:
    maxv=max(maxv,i.pdgrp)


b=flipitems.objects.filter().all()
for i in b:
    if i.pdgrp==0 and i.spid.strip():
       c=amznitems.objects.filter(id=i.spid).all()
       if c:
         if c[0].pdgrp>0:
             i.pdgrp=c[0].pdgrp
         else:
            maxv=maxv+1
            c[0].pdgrp=maxv
            i.pdgrp=maxv
            c[0].save()
       i.save()
       c=snapitems.objects.filter(spid=i.spid).all()
       for j in c:
        if j.pdgrp==0:
         j.pdgrp=i.pdgrp
         j.save()
       c=flipitems.objects.filter(spid=i.spid).all()
       for j in c:
        if j.pdgrp==0:
         j.pdgrp=i.pdgrp
         j.save()
       c=infiitems.objects.filter(spid=i.spid).all()
       for j in c:
        if j.pdgrp==0:
         j.pdgrp=i.pdgrp
         j.save()
       c=ptmitems.objects.filter(spid=i.spid).all()
       for j in c:
        if j.pdgrp==0:
         j.pdgrp=i.pdgrp
         j.save()
       
