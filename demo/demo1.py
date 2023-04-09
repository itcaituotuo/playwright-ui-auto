# author: 测试蔡坨坨
# datetime: 2023/4/8 2:18
# function: 第一个playwright脚本，使用with写法

from playwright.sync_api import sync_playwright, expect


def run(playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)  # headless表示是否使用无头浏览器（也就是无GUI模式）
    page = browser.new_page()
    page.goto("https://caituotuo.top")
    # other actions...
    print(page.title())
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

# 这里使用的是with方法，Python中的with方法可以很方便处理一些需要提前设置，事后需要清理的工作
# playwright正好有上下文处理，所以使用with写法会使代码更加简洁
# 比如：
# with open("/caituotuo.txt") as f:
#     f.read()
#
# 非with方式可能存在问题：1.可能忘记关闭文件句柄 2.文件读取数据时发生异常，但是没有进行任何处理
# f = open("/caituotuo.txt")
# data = f.read()
# f.close()
