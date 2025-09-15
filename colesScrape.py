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
# print(soup.prettify)

table = soup.find_all('table', {'class': 'sc-9fe53a46-2 heRyOF coles-targeting-TableTableContainer'})[0]
headers = []
rows = []
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        headers.append([el.text.strip() for el in row.find_all('th')])
    else:
        rows.append([el.text.strip() for el in row.find_all('th')])
        rows.append([el.text.strip() for el in row.find_all('td')])
print(headers)
print(rows)

