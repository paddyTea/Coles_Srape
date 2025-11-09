import requests
from bs4 import BeautifulSoup
import pickle
import re
from goodsClass import Good
import goodsClass
from pathlib import Path


# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')

filename = "HTML_Storage_Monster"
try:
    with open(Path(__file__).parent/"HTMLStorage"/filename, "rb") as file:
        HTMLStorage = pickle.load(file)
        print(f"Success loading {filename}.")
except Exception as e:
    print(f"Error loading object: {e}")

soup = HTMLStorage
#Check to see if nutition information is present for product
#If true extract necessary information to create good objecct
#If false display message
if "nutrition" in HTMLStorage.prettify():
    # Product Name
    name = soup.find(class_='product__title').text
    print("Name: ",name)

    # Product Price
    price = soup.find(class_='price').text
    print("Price: ", price)
    
else: print("Not food / No nutrition information")
