import sys
from datetime import datetime

import eventlet

import settings
from models import ProductRecord
from helpers import make_request, log, format_url, enqueue_url, dequeue_url
from extractors import get_title, get_url, get_price, get_primary_img,get_container

crawl_time = datetime.now()
cate=['Laptop bags','rucksacks','school bags','cabin luggage','check in luggage','travel duffles','travel accessories','briefcases','wallet for men','handbags','slingbags']


def fetch_listing():
 for j in cate:
  for brands in brnds:
    url="https://www.infibeam.com/laptop-bags/search?q="+j+"&us=nbc#make="+brands
    global crawl_time
    page, html = make_request(url)
    if not page:
        return
    items = get_container(page)
    log("Found {} items on {}".format(len(items), url))
    for item in items[:settings.max_details_per_listing]:

        product_url = get_url(item)
        product_price = get_price(item)

        product = ProductRecord(
      
            product_url=format_url(product_url),
            listing_url=format_url(url),
            price=product_price,
            
            crawl_time=crawl_time

        )
        product_id = product.save()
        # download_image(product_image, product_id)

    # add next page to queue
    


if __name__ == '__main__':
    log("Beginning crawl at {}".format(crawl_time))
    fetch_listing()
  
