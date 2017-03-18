from bs4 import BeautifulSoup
import urllib2




headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
   }
url="http://www.amazon.in/gp/product/B01J5K7RPQ"
res=urllib2.urlopen(url)
#request = requests.get(url, headers=headers)
br=BeautifulSoup(request.read(),"html.parser")
pr = br.findAll("span", {'id':"priceblock_ourprice"})

from bs4 import BeautifulSoup
import urllib2
import re
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
   }
url="http://dl.flipkart.com/dl/american-tourister-amt-2016-encarta-laptop-backpack/p/itmegnymuswctxuu?pid=BKPEGNYMVMFJZSYS"
reqt = urllib2.Request(url, headers=headers)
reqt1=urllib2.urlopen(reqt)

price=re.match(".*\"price\" *\: *([0-9]*),.*",reqt1.read())
if price:
     print price.group(1)+","
             
