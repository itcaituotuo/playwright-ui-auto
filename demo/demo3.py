# author: 测试蔡坨坨
# datetime: 2023/4/8 20:39
# function:

import asyncio

from playwright.async_api import async_playwright


async def run(playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("https://caituotuo.top")
    # other actions...
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
