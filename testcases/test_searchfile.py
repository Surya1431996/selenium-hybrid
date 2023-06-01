import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_html

from pages.HomePage import HomePage
from utilities.customlogger import LogGen


@pytest.mark.usefixtures("setup")
class Testsearch:
    logger = LogGen.Loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_for_valid_product(self):
        self.logger.info("*****************Testsearch started****************************")
        self.logger.info("*****************product search started************************")
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        home_page.click_on_search_button()
        assert home_page.display_status_of_hp_product()
        self.logger.info("********************product is displayed***************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_for_invalid_product(self):
        self.logger.info("*****************invalid product search started************************")
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("honda")
        home_page.click_on_search_button()
        expe_msg = "There is no product that matches the search criteria."
        assert home_page.display_status_of_product().__eq__(expe_msg)
        self.logger.info("********************product is not displayed***************************")
