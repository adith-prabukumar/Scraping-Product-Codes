import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import uuid

import json
import urllib.parse as urlparse
from urllib.parse import parse_qs
from urllib.parse import urlparse
from urllib.request import urlopen
import time
import re


proxy_headers = {
    'x-rapidapi-key': "c648578396msh61ff21c67f4c149p177a03jsn35abba913cb9",
    'x-rapidapi-host': "proxy-orbit1.p.rapidapi.com"
    }

def UPC_2_ItemId(upc):
    
    my_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
              + "(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    url= "https://www.walmart.com/search/?query=" + str(upc)
    
    
    
    r= requests.get(url, headers= my_header)
    if r.status_code==200:
        soup_main= BeautifulSoup(r.content, 'lxml')
        #print(soup_main)
        summary=soup_main.find('div', {'class':'search-product-result', 'id':'searchProductResult'})
        #print(summary)
        product_list= summary.find_all('a')
        #print(product_list)
        try:
            
            item_url= product_list[0].get('href')
            product_code= item_url.split('/')[-1]
            
        except:
            print("THIS WAS USEd")
            pass
    else:
        print("Error-",r.status_code)
    
    return product_code

def ItemId_2_UPC(item_id):
    item_url= 'https://www.walmart.com/reviews/product/'+ str(item_id) +'?page=2'
    r = requests.get(item_url,headers=proxy_headers)



    soup = BeautifulSoup(urlopen(item_url),'html.parser')
    for val in soup.find_all("script"):
   
        if 'upc' in str(val):
            val=str(val)
            prob_dict = val.split('upc')[1]
            UPC=prob_dict.split(',')[0]
            UPC=UPC[3:-1]
            prob_dict = val.split('productName')[1]
            product=prob_dict.split(',')[0]
            product=product[3:-1]
            
            return UPC, product

def UPC_2_ASIN(upc):
    
    request_url = 'https://ar4vkdr7il.execute-api.us-east-1.amazonaws.com/test'

    url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+ str(upc)
    
    
    payload ={}
    payload["url"] = url
    payload["delay"] = '5'

    payload = json.dumps(payload)
    
    headers = {
       
       'content-type': "application/json",
       'accept': "application/json"
    }

    
    r = requests.post(request_url,data=payload, headers=headers )
    r.status_code
    
    raw_response = json.loads(r.text)
    
    
    soup = BeautifulSoup(raw_response["body"],'html.parser')

    item_url=soup.find_all('a',{'class':"a-link-normal a-text-normal"})
    for x in item_url:
        
        if("/dp/" in x.get("href")):

            asin= x.get("href").split("/")[3]        
            product_name=x.span.text
            
            return asin, product_name
        
        
if __name__=="__main__":
    
    print("Walmart Item ID: ",UPC_2_ItemId(753048414284))

    print(ItemId_2_UPC(20893651))

    print(UPC_2_ASIN(753048414284))
