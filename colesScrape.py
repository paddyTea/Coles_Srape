import requests
from bs4 import BeautifulSoup
import pickle
import re

# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')
filename = "HTML Storage"
try:
    with open(filename, "rb") as file:
        HTMLStorage = pickle.load(file)
        print(f"Success loading {filename}.")
except Exception as e:
    print(f"Error loading object: {e}")

soup = HTMLStorage
# print(soup.prettify)

# Product Name
name = soup.find(class_='product__title').text
# print("Name: ",name)

# Product Price
price = soup.find(class_='price').text
print("Price: ", price)

# Pricer per
str_price_per = soup.find(class_='sc-79c0c972-0 jowmDW').text
print("Price per: ", str_price_per)

# nutrition table scrape and display
table = soup.find_all('table', {'class': 'sc-9fe53a46-2 heRyOF coles-targeting-TableTableContainer'})[0]
headers = []
rows = []
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        headers.append([el.text.strip() for el in row.find_all('th')])
        # rows.append([el.text.strip() for el in row.find_all('th')])
    else:
        label = [el.text.strip() for el in row.find_all('th')]
        values = [el.text.strip() for el in row.find_all('td')]
        rows.append(label + values)
# print("Nurtrition Information:")
# print(headers)
# for r in rows:
#     print(r)

# print(rows[0][1])


ppnumberList = re.findall(r'\d+', str_price_per)
int_price_per = int(ppnumberList[0])+(int(ppnumberList[1])/100)
print("String Price Per: ", str_price_per)
print(ppnumberList)
print("int_price_per: ", int_price_per)

#Convert from per KG or L to per 100g or 100ml 
if(ppnumberList[-1]) == '1':
    int_price_per_100 = float(int_price_per/10)
print("Price Per 100: ", int_price_per_100)


# Int price
numberList = re.findall(r'\d+', str_price_per)
int_price = int(numberList[0])+(int(numberList[1])/100)
print("int_price: ", int_price)

# how many hundreds of grams or ml in the product
weight_in_100 = int_price/int_price_per_100
print("weight_in_100: ", weight_in_100)
print(type(weight_in_100))