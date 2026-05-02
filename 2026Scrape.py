import asyncio
import random
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
import pandas as pd

async def get_session_data():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        page = await context.new_page()

        
        current_url = f"https://www.coles.com.au"
        await page.goto(current_url, wait_until="domcontentloaded")


if __name__ == "get_session_data":
    asyncio.run(get_session_data())

 