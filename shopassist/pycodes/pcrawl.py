amazon sitemaps
for i in sitemaps:
    j=request(i)
    for i1 in j.etree:
        k=i1(.//items) //what items? 
        for i2 in k:
         extractitems()
    for i1 in j.links:
        if i1 not in donelinks:
            if i1 suitable:  #define suitable
                urls.add(i1)
    urls.remove(j)
    donelinks.append(j)
    
                 

            


