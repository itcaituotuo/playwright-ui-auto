# author: 测试蔡坨坨
# datetime: 2023/4/10 0:13
# function:
import time

import pytest
from playwright.sync_api import sync_playwright

from utils.config_utils import ConfigUtils


@pytest.fixture(scope='function')
def access_web():
    """
    访问web
    :return:
    """
    playwright = sync_playwright().start()
    # "chromium" or "firefox" or "webkit"
    # headless表示是否使用无头浏览器（也就是无GUI模式）
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(ConfigUtils().get_url())
    yield page
    time.sleep(3)
    print('执行结束')
