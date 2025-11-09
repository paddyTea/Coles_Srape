from bs4 import BeautifulSoup
import pickle
from pathlib import Path
import csv
filename = "HTML_Storage_Page_DownDown1"
try:
    with open(Path(__file__).parent/"HTMLStorage"/filename, "rb") as file:
        HTMLStorage = pickle.load(file)
        print(f"Success loading {filename}.")
except Exception as e:
    print(f"Error loading object: {e}")

soup = HTMLStorage

file = open("urlList.csv","w")
#cycles through html, collects all product hyperlinks
for a in soup.find_all('a', href=True):
    if "/product/" in a['href']:
        writer = csv.writer(file)
        writer.writerow(["www.coles.com.au"+a['href']])
        print("Found the URL:", a['href'])
file.close()