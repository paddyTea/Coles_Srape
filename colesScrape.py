import requests
from bs4 import BeautifulSoup

url = 'https://www.coles.com.au/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
print(page.status_code)

print(soup.prettify)
