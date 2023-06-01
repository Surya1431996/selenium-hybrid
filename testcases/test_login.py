from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

from pages.login import LoginPage


@pytest.mark.usefixtures("setup")
class Testlogin:
    def test_search_for_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_into_login_filed()
        login_page.enter_to_email_field("teja999@gmail.com")
        login_page.enter_to_password_field("1234567")
        login_page.enter_to_login_field()
        assert login_page.enter_to_verify()

    def test_search_for_valid_email_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.enter_into_login_filed()
        login_page.enter_to_email_field("teja999@gmail.com")
        login_page.enter_to_password_field("123456")
        login_page.enter_to_login_field()
        warnmsg = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.enter_to_verify_valid_text().__contains__(warnmsg)

    def test_search_for_invalid_email_valid_password(self):
        login_page = LoginPage(self.driver)
        login_page.enter_into_login_filed()
        login_page.enter_to_email_field("teja99@gmail.com")
        login_page.enter_to_password_field("123456")
        login_page.enter_to_login_field()
        warnmsg = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.enter_to_verify_valid_text().__contains__(warnmsg)


