# author: 测试蔡坨坨
# datetime: 2023/4/10 0:17
# function:

import pytest
from pages.app.login_page import LoginPage
from business.app.biz_login import BizLogin


class TestLogin:
    @pytest.mark.usefixtures('access_web')
    def test1(self, access_web):
        obj = BizLogin(access_web)
        obj.login()
