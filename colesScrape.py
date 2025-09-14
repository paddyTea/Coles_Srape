import requests

response = requests.get('https://www.coles.com.au/product/coles-no-added-hormone-beef-3-star-regular-mince-1kg-9012825')

print(response.status_code)

print(response.text)