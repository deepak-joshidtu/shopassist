#import json
#import urllib2
import MySQLdb

conn = MySQLdb.connect("103.50.160.63","hotbuy5g_joshi","joshi123","hotbuy5g_prdctlist" )
#conn = psycopg2.connect(database=settings.database, host=settings.host, user=settings.user)
cur = conn.cursor()
#cur.execute("DROP TABLE IF EXISTS paytmproducts")
#cur.execute("""CREATE TABLE paytmproducts(
 #  id          serial PRIMARY KEY,
  #     product_url         varchar(2056),
   #    image_url         varchar(2056),
        #listing_url varchar(2056),
    #    price       varchar(128),
     #   brand       varchar(128),
      #  name      varchar(1000)
       #)""")
#conn.commit()
"""f=open('paytm_links','r')
lst=[]
import re
for i in f:
  if i.strip():
   k=i.replace("https://paytm.com/shop/","https://catalog.paytm.com/v1/")
   lst.append(k[:-1])"""
#for i in lst:
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
}
for i in range(201,300):
   print i
   #https://paytm.com/shop/g/men/accessories/bags
   url = "https://catalog.paytm.com/v1/g/men/bags?channel=web&child_site_id=1&site_id=1&version=2&page_count="+str(i)+"&items_per_page=30&resolution=960x720&quality=high&curated=1&_type=1"
#" /g/men/bags/backpacks from sitemap
   #url=i+
   request = urllib2.Request(url, headers=headers)
   try:
      data = json.load(urllib2.urlopen(request))
   except urllib2.HTTPError:
       print "haha ereor"
       break
   if not data:
       break
#   data['grid_layout'][1]
   for  j in data['grid_layout']:
     
        try:
           print j['product_id']
           print j['name']
           print j['offer_price']
           print j['url']
           print j['image_url']
           print re.sub('[^a-zA-Z0-9\.]+', '',j['brand'])
           cur.execute("INSERT INTO paytmproducts( product_url, image_url, price,brand,name) VALUES  (%s,%s, %s, %s, %s) ", (
            j['url'],
            j['image_url'],
            j['offer_price'],
            re.sub('[^a-zA-Z0-9\.]+', '',j['brand']),
            re.sub('[^a-zA-Z0-9\.]+', '',j['name']),
           ))
        except UnicodeEncodeError,cur.ProgrammingError:
            print "error at haha"
        conn.commit() 
       

