from selenium import webdriver
import undetected_chromedriver as uc

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import pickle

options = uc.ChromeOptions()
options.headliess = False

# options.add_experimental_option("detach", True)
# options.add_argument("--headless")

# options = Options()
driver = uc.Chrome(options=options)  

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option(
#     "prefs", {"profile.managed_default_content_settings.images": 2}
# )
with driver:
    driver.get("https://www.coles.com.au/product/coles-adult-dry-dog-food-with-beef-8kg-5075277?uztq=46abcbb7e16253b0cdc3e6c5bbe6a3f0&cid=col_cpc_Generic%7CColesSupermarkets%7CPLA%7CPet%7CAustralia%7CBroad&s_kwcid=AL!12693!3!683434678447!!!g!295782145136!&gclsrc=aw.ds&gad_source=1&gad_campaignid=20838080077&gbraid=0AAAAADzlvJeCVDGJPNajTePiumTQC8FHT")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

filename = "HTML_Storage_DogFood"
try:
    with open(filename, "wb") as file:
        pickle.dump(soup, file)
    print("Successful Dump", filename)
except Exception as e:
    print("Error during pickling object (Possibly unsupported):", {e})

print(soup.prettify())
print(filename)
driver.close()