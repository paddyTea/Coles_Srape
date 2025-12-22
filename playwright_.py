import asyncio
import random
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
import pandas as pd

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        page = await context.new_page()

        await stealth_async(page)
        
        all_urls=[]
        idx = 1

        current_url = f"https://www.coles.com.au/browse/down-down"
        await page.goto(current_url, wait_until="domcontentloaded")

        try:
            # Go to the site
            while True:
                #mimic human behavour
                wait_time = random.uniform(3, 7)
                await page.wait_for_timeout(wait_time * 1000)
                
                #Find urls using classes
                product_locator = page.locator("a.product__link.product__image")
                elements = await product_locator.all()
                
                # break if you dont find an element
                if len(elements) == 0:
                    print(f"No more products found. Finished at page {idx-1}.")
                    break
                
                #Add Urls to all_URL list
                urls = [await el.get_attribute("href") for el in elements]
                all_urls = all_urls + urls
                idx = idx + 1
                next_button = page.get_by_label("Go to next page")
                await next_button.scroll_into_view_if_needed()
                await page.wait_for_timeout(random.uniform(1000, 2000)) # Human hesitation
                await next_button.click()
                #break if you go to page 14
                if idx > 14: 
                    print("Reached page 14 and quit")
                    print(f"Saved {len(all_urls)} URLs")
                    break
                
        except Exception as e:
            print(f"Blocked or Error on attempt: {e}")




if __name__ == "__main__":
    asyncio.run(main())

 
