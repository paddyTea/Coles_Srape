import requests
import math
from bs4 import BeautifulSoup
import math
import time

import json

import undetected_chromedriver as uc

# options = uc.ChromeOptions()
# options.headless = False
# driver = uc.Chrome(options=options)  

# driver.get("https://www.coles.com.au")
# html = driver.page_source
# print(len(html))


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 OPR/132.0.0.0"
}

def get_buildID():
    url = "https://www.coles.com.au"

    options = uc.ChromeOptions()
    options.headless = False
    driver = uc.Chrome(options=options)  

    driver.get(url)
    time.sleep(10)
    html = driver.page_source
    try:
        driver.quit()
    except:
        pass

    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find("script", {"id": "__NEXT_DATA__"})
    NEXT_DATA_dict = json.loads(tag.string)
    buildID = NEXT_DATA_dict["buildId"]

    return buildID

buildId = get_buildID()
print(buildId)


url = f"https://www.coles.com.au/_next/data/{buildId}/en/browse/meat-seafood.json?slug=meat-seafood"

html = requests.get(url, headers=headers)

print(html.status_code)
# print(html.text)
data = html.json()

noOfResults = data["pageProps"]["searchResults"]["noOfResults"]
pageSize = data["pageProps"]["searchResults"]["pageSize"]
NumOfPage = math.ceil(noOfResults/pageSize)


for x in range(NumOfPage):
    print(x+1)
    url = f"https://www.coles.com.au/_next/data/{buildId}/en/browse/meat-seafood.json?page={x+1}slug=meat-seafood"
            
    html = requests.get(url, headers=headers)
    data = html.json()

    products = data["pageProps"]["searchResults"]["results"]
    for product in products:
        if product["_type"] == "PRODUCT" and product["availability"] == True:  
            name = product["name"]
            price = product["pricing"]["now"]
            print(f"{name}: ${price}")
    print(f"page {x+1} scanned")







  
