
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import pickle

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")

# options = Options()
driver = webdriver.Chrome(options=options)  

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option(
#     "prefs", {"profile.managed_default_content_settings.images": 2}
# )

driver.get("https://www.coles.com.au/product/indomie-fried-bbq-chicken-instant-noodles-5x85g-425g-7398277?uztq=46abcbb7e16253b0cdc3e6c5bbe6a3f0&cid=col_cpc_Generic%7CColesSupermarkets%7CPLA%7CPantry%7CAustralia%7CBroad&s_kwcid=AL!12693!3!683434678444!!!g!1958148715884!&gclsrc=aw.ds&gad_source=1&gad_campaignid=20838080074&gbraid=0AAAAADzlvJchDmHuRBUWgYfmuwpD65UhI")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

filename = "HTML_Storage_MiGoreng"
try:
    with open(filename, "wb") as file:
        pickle.dump(soup, file)
    print("Successful Dump", filename)
except Exception as e:
    print("Error during pickling object (Possibly unsupported):", {e})

print(soup.prettify())
print(filename)
driver.close()