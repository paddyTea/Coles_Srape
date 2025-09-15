import requests
from bs4 import BeautifulSoup
import pickle

# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')
filename = "HTML Storage"
try:
    with open(filename, "rb") as file:
        HTMLStorage = pickle.load(file)
        print(f"Success loading {filename}")
except Exception as e:
    print(f"Error loading object: {e}")

soup = HTMLStorage
print(soup.prettify)
