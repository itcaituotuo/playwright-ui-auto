# author: 测试蔡坨坨
# datetime: 2023/4/8 2:18
# function: 使用start()写法，直接实例化playwright同步方法

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
chromium = playwright.chromium  # or "firefox" or "webkit".
browser = chromium.launch(headless=False)  # headless表示是否使用无头浏览器（也就是无GUI模式）
page = browser.new_page()
page.goto("https://caituotuo.top")
# other actions...
print(page.title())
browser.close()
