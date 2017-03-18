ctl=['laptop','briefcase','trolly','cabin','duffle','handbag','wallet','sling','school','messenger']
dictl={'laptop':'Laptop bags','briefcase':'briefcases','trolly':'cabin luggage','cabin':'cabin luggage','duffle':'travel duffles','handbag':'handbags','wallet':'wallet for women','sling':'slingbags','school':'school bags','messenger':'messenger bags'}
from polls.models import infiitems,snapitems,ptmitems
for i in ctl:
    a=snapitems.objects.filter(allkeyw__icontains=i).all()
    f=open("brands/"+dictl[i].replace(" ","_"),'r')
    for j in f:
        k=j.split(",")
    print len(a)
    for j in a:
       for ji in k:
           if ji.split():
              
              if ji.lower() in j.allkeyw:
                   
                   bc=dictl[i].replace(" ","_")+ji
                   if bc not in j.brandcategory:
                        j.brandcategory=j.brandcategory+","+bc
                        j.save()
                        print j.brandcategory
        
        

db.runCommand({renameCollection:"test1.snapitems",to:"test.snapitems"})
db.polls_ptmitems.find().forEach(function(d){ db.getSiblingDB('test')['polls_ptmitems'].insert(d); });
