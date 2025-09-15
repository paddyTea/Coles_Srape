
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import re

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# options = Options()
driver = webdriver.Chrome(options=options)  

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option(
#     "prefs", {"profile.managed_default_content_settings.images": 2}
# )

driver.get("https://www.coles.com.au/product/coles-no-added-hormone-beef-3-star-regular-mince-1kg-9012825")

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
# print (soup.prettify())

table = soup.find_all('table', {'class': 'sc-9fe53a46-2 heRyOF coles-targeting-TableTableContainer'})[0]

headers = []
rows = []
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        headers = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

print(headers)
print(rows)
