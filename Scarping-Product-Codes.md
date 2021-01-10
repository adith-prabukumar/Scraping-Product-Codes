# Scraping-Product-Codes
*What are product codes? What are its types? Why are product codes used?*

A product code describes a specific product and contains a combination of five to seven numbers and letters. These are the codes that are usually on the back of the product. These codes are important mainly due to its unique nature.

## Types of Product Codes

**UPC**:
Universal Product Code (UPC) is a 12-digit bar code used extensively for retail packaging in the United States.
A typical process of obtaining a 12-digit UPC number is as follows:
- License a unique Company Prefix from your local GS1 office. GS1 is a not-for-profit organisation that develops and maintains global standards for business communication.
- Assign product number(s) to unique products making your number equal 11 digits
- Using a check digit calculator with your 11 digit number, generate your check digit.

**EAN**:
The European Article Number (EAN) is a barcode standard, a 12- or 13-digit product identification code. Each EAN uniquely identifies the product, manufacturer, and its attributes;
typically, the EAN is printed on a product label or packaging as a bar code. We require EAN codes to improve the quality of search results and the quality of the catalogue as a
whole.

**ISBN**:
The International Standard Book Number (ISBN) is a unique commercial book identifier barcode. Each ISBN code identifies uniquely a book. ISBN have either 10 or 13 digits.
Typically, the ISBN is printed on the back cover of the book.

**ASINs**:
Amazon Standard Identification Numbers (ASINs) are unique blocks of 10 letters and/or numbers that identify items. You can find the ASIN on the item's product information page at
Amazon.com. For books, the ASIN is the same as the ISBN, but for all other products, a new ASIN is created when the item is uploaded to our catalogue.



These are the commonly used types of codes. But many stores have product codes of their own. For Example, the product *Invicta Men's Pro Diver Scuba 48mm Gold Tone Stainless Steel
Quartz Watch* is available on Walmart with a product code- 39825323. But this product has a UPC-843836069830. The UPC code is used to find the product regardless of the platform 
from which it's being sold on.

[https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=843836069830](https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=843836069830)

[https://www.walmart.com/search/?query=843836069830](https://www.walmart.com/search/?query=843836069830)

clicking on the first result, you will get [https://www.walmart.com/ip/Invicta-Men-s-Pro-Diver-6983-Gold-Rubber-Swiss-Chronograph-Fashion-Watch/39825323](https://www.walmart.com/ip/Invicta-Men-s-Pro-Diver-6983-Gold-Rubber-Swiss-Chronograph-Fashion-Watch/39825323)



## How to Get UPC Product Codes?

### Online Converter:
There are several data providers that take product URLs and convert them the corresponding Code to a UPC code. Some of these are:


[algopix.com](algopix.com)

By simply entering a keyword or product description, you can view product images and metadata, which can help you better describe your merchandise. You also receive a complete
summary of how similar products are being sold on various marketplaces.

This product contains a free plan for amazon approved sellers. Rest must opt for a $27.99/month package.

[synccentric.com](synccentric.com)

This is primarily ASIN to UPC or UPC to ASIN converter. Import your UPCs or ASINs along with any other custom data. The system then searches for the products that match the
uploaded ASINs or UPCs and returns as much data as possible including identifiers (ASIN, UPC, MPN, SKU, EAN, ISBN), pricing (buy box, shipping, lowest pricing for FBA and
Merchant, list pricing), sales rank, and other product listing data.

This conversion feature is free although a fee of $39.99/ month must be paid for the site to provide analytics and access to the API.

[asinscope.com](asinscope.com)

This is similar to the synccentric, wherein they do various bulk conversions. The price to access this API is $25/month

## UPC Databases

The above sites provide product analytics and information of product across the various platforms it is being sold on.
There are also large databases that contain UPCs and we can search through them. One particular example of it is [barcodelookup.com](barcodelookup.com)
Here all we need to do is type in the UPC and we get details on the product. It is shown below as we search a product with UPC 843836069830

Some other websites that do a similar function are [www.upcitemdb.com](www.upcitemdb.com), [scandit.com/upc-lookup](scandit.com/upc-lookup), [barcodesdatabase.org](barcodesdatabase.org)


## How to scrape UPC codes?

UPC codes can be found on all the product websites if you look close enough. Every product contains a dictionary which includes all product info- name, price, description,
product code, upc etc.

In the case of Walmart, this can be found in the product reviews page source. We can then call a parser to parse this and collect the dictionary and collect the upc from this.

The python code block is illustrated below:

    import requests
    import json
    from bs4 import BeautifulSoup
    
    url = 'https://www.walmart.com/reviews/product/43928713?page=2'
    r = requests.get(url,headers=proxy_headers)

    r.status_code

    soup = BeautifulSoup(r.text,'html.parser')
    for val in soup.find_all("script"):
        if 'upc' in val.text:
            prob_dict = val.text.split('window.__WML_REDUX_INITIAL_STATE__ = ')[1]

    for k,v in json.loads(prob_dict.strip()[:-1])["product"]["products"].items():
        product_code = k
        print(json.loads(prob_dict.strip()[:-1])["product"]["products"][k]["upc"])
