from selenium.webdriver.common.by import By
import time


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search_box_field_name = "search"
    search_button_xpath = "//*[@id='search']/span/button"
    valid_hp_product_link_text = "HP LP3065"
    invalid_product_msg_xpath = "//*[@id='content']/p[2]"

    def enter_product_into_search_box_field(self, product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        time.sleep(2)
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)
        time.sleep(2)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        time.sleep(2)

    def display_status_of_hp_product (self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_hp_product_link_text).is_displayed()
        time.sleep(2)


    def display_status_of_product(self):
        return self.driver.find_element (By.XPATH, self.invalid_product_msg_xpath).text
        time.sleep(2)





