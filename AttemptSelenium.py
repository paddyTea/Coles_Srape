from selenium import webdriver
import undetected_chromedriver as uc

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import pickle
import time
from selenium.webdriver.common.by import By
import csv

options = uc.ChromeOptions()
options.headless = False

# options.add_experimental_option("detach", True)
# options.add_argument("--headless")

# options = Options()
driver = uc.Chrome(options=options)  

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option(
#     "prefs", {"profile.managed_default_content_settings.images": 2}
# )

filename = "HTML_Storage_Page_DownDown1"

with driver:
    driver.get("https://www.coles.com.au/browse/down-down")

################### This is where you are working###############
#just reliased the pages have differnet urls, 1,2,3...ect
# while(driver.find_element(By.CSS_SELECTOR,'a[aria-label="Go to next page"]')):



html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
try:
    with open(filename, "wb") as file:
        pickle.dump(soup, file)
    print("Successful Dump", filename)
except Exception as e:
    print("Error during pickling object (Possibly unsupported):", {e})

file = open("MyCSVFile.csv","w")
writer = csv.writer(file)
writer.writerow(["test"])
file.close()

# driver.save_screenshot('downdown1.png')

print(soup.prettify())
print(filename)
# driver.close()
