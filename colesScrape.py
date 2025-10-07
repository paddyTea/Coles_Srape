import requests
from bs4 import BeautifulSoup
import pickle
import re
from goodsClass import Good
from pathlib import Path


# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')

filename = "HTML_Storage_DogFood"
try:
    with open(Path(__file__).parent/"HTMLStorage"/filename, "rb") as file:
        HTMLStorage = pickle.load(file)
        print(f"Success loading {filename}.")
except Exception as e:
    print(f"Error loading object: {e}")

soup = HTMLStorage
print(soup.prettify())

# Product Name
# name = soup.find(class_='product__title').text
# print("Name: ",name)

# # Product Price
# price = soup.find(class_='price').text
# # print("Price: ", price)

# # Pricer per
# price_per = soup.find(class_='sc-79c0c972-0 jowmDW').text
# # print("Price per: ", price_per)

# # nutrition table scrape and display
# table = soup.find_all('table', {'class': 'sc-9fe53a46-2 heRyOF coles-targeting-TableTableContainer'})[0]
# headers = []
# rows = []
# for i, row in enumerate(table.find_all('tr')):
#     if i == 0:
#         headers.append([el.text.strip() for el in row.find_all('th')])
#         # rows.append([el.text.strip() for el in row.find_all('th')])
#     else:
#         label = [el.text.strip() for el in row.find_all('th')]
#         values = [el.text.strip() for el in row.find_all('td')]
#         rows.append(label + values)

# instance = Good(name,price,price_per,rows)
        
# print(instance.name)
# print("Nurtrition Information:")
# print(headers)
# for r in rows:
#     print(r)
