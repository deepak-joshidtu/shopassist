from polls.models import amzntables
from difflib import SequenceMatcher as SM
b=['Laptop bags','wallet for women','handbags','slingbags','tote bags','check in luggage','Laptop bags','rucksacks','school bags','cabin luggage','travel duffles','travel accessories','messenger bags','briefcases','wallet for men']
features=[]
featurelabels=[]
for i in b:
    brndl=[]
    bnds=amznitems.objects.filter(brandcategory__icontains=i.replace(" ","_")).all()
    cnt=0
    for j in bnds:       
           tem=j.brandcategory.replace(i.replace(" ","_"),"")
           sc=SM(None, tem, j.brand).ratio()
           if sc <0.8:
              j.blk=1
              j.save()
        for k in range(cnt+1:len(bnds)):
            simscore=0
            l=bnds[k]
            n1=j.amzlink
            name=re.match(r'.*\.in/(.*)/dp.*',n1).group(1)
            n1=l.amzlink
            name1=re.match(r'.*\.in/(.*)/dp.*',n1).group(1)
            namematch=SM(None, name, name1).ratio()
            pricematch=min(j.price,l.price)/max(j.price,l.price)
            colormatch=SM(None, j.color, l.color).ratio()
            featurematch=SM(None, j.features, l.features).ratio()
            titlematch=SM(None, j.title, l.title).ratio()
#            heightmatch=min(j.height,l.height)/max(j.height,l.height)
 #           widthmatch=min(j.width,l.width)/max(j.width,l.width)
            dimensionmatch=min(j.length+j.height+j.width,l.length+l.height+l.width)/max(j.length+j.height+j.width,l.length+l.height+l.width)
            productgroupmatch=SM(None, j.productgroup, l.productgroup).ratio()
            departmentmatch=SM(None, j.department, l.department).ratio()
            bindingmatch=SM(None, j.binding, l.binding).ratio()
            features.append([namematch,pricematch,featurematch,titlematch,dimensionmatch,asinmatch,imagematch,productgroupmatch,  departmentmatch,bindingmatch])
            if(j.id in k.spid or k.spid in j.id or k.spid in j.spid):
                 featurelabels.append(1)
            else:
                 featurelabels.append(0)


from sklearn import svm
X = features
y = featurelabels
clf = svm.SVC()
clf.fit(X, y)  

