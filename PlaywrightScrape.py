from playwright.sync_api import sync_playwrite
import pandas as pd
import time

#create scraper function
def scraper(playwright):
    browser = playwright.chronium.launch_persistent_context(
        user_data_dir="C:\playwright",
        channel="chrome",
        headless=False,
        no_viewport=True
    )

#initiate page
page  = browser.new_page()

#keep track of page count
page_count = 1

products =[]

while page_count < 2:
    print("Scraping page "+page_count)
    time.sleep(2)
    page.goto()