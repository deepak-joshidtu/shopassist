from polls.models import ptmitems,snapitems,infiitems
a=infiitems.objects.filter().all()
import re
for i in a:
    b=re.sub('[^a-zA-Z ]+', '',i.amzlink).lower()
    b+=re.sub('[^a-zA-Z ]+', '',i.list_url).lower()
    b+=i.title.lower()
    b+=i.features.lower()
    i.allkeyw=b
    i.save()

