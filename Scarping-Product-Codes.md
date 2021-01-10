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

The python code block on scraping the first 10 pages of walmart products is illustrated below:

Here we scrape the watches UPC from walmart:

        my_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
              + "(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

        querystring = {"page":"10", 'product_url':'https://www.walmart.com/search/?query=watch'}
        item_url=[]

        total_pages=int(querystring["page"])


        for i in range(1,total_pages+1):
    
            url='https://www.walmart.com/search/?page='+ str(i) +'&ps=48&query=watches'
            r= requests.get(url, headers= my_header)
            price_per_page=[]
            if r.status_code==200:
                soup_main= BeautifulSoup(r.content, 'html')
                
                summary=soup_main.find('div', {'class':'search-product-result', 'id':'searchProductResult'})
                product_list= summary.find_all('li')
                for prod in product_list:
                    try:
                        item_url.append(prod.find('a', {"class":"product-title-link line-clamp line-clamp-2 truncate-title"}).get('href'))
                    except:
                        pass
            else:
                print("Error-",r.status_code)

        product_code=[u.split('/')[-1] for u in item_url]
    
The variable Product code contains all the walmart product codes of the products in the first 10 pages. Now We will loop through these pages to get the UPCs

        upc=[]
        item_ID=[]
        product_name=[]
        for prod_code in product_code:
            item_url= 'https://www.walmart.com/reviews/product/'+ prod_code +'?page=2'
            r = requests.get(item_url,headers=proxy_headers)

            r.status_code

            soup = BeautifulSoup(urlopen(item_url),'html.parser')
            for val in soup.find_all("script"):
                #print(val)
                if 'upc' in str(val):
                    val=str(val)
                    prob_dict = val.split('upc')[1]
                    UPC=prob_dict.split(',')[0]
                    UPC=UPC[3:-1]
                    upc.append(UPC)
                    prob_dict = val.split('usItemId')[1]
                    item_id=prob_dict.split(',')[0]
                    item_id=item_id[3:-1]
                    item_ID.append(item_id)
                    prob_dict = val.split('productName')[1]
                    product=prob_dict.split(',')[0]
                    product=product[3:-1]
                    product_name.append(product)

Doing this will give us a data base of product name and its corresponding walmart code and upc.

                df_dict={"Product Name": product_name, "Walmart Product Code": item_ID, "UPC": upc}
                df=pd.DataFrame(df_dict)
                df.to_csv("UPCs of Walmart Watches")
                
                
## Conclusion

Here we saw what Product codes are and its different types- UPC, EAN, ASIN, ISBN. We also saw data providers that analyse products from various platforms to see its trends and
gain insights. We also looked the various UPC databases and checked how we can create these databases of our own. 
