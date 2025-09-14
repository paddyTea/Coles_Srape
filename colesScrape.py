import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.coles.com.au/product/coles-no-added-hormone-beef-3-star-regular-mince-1kg-9012825')

soup = BeautifulSoup(response.content, 'html.parser')

print(response.status_code)

print(soup.prettify())

# print(response.text)

