
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import pickle

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
soup = BeautifulSoup(html, 'html.parser')

# filename = "HTML Storage"
# try:
#     with open(filename, "wb") as file:
#         pickle.dump(soup, file)
#     print("successful Dump")
# except Exception as e:
#     print("Error during pickling object (Possibly unsupported):", {e})



