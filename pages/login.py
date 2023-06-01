from selenium.webdriver.common.by import By
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    account_link_text = "My Account"
    log_link_text = "Login"
    email_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//*[@id='content']/div/div[2]/div/form/input"
    valid_login_link_text = "Edit your account information"
    valid_text_xpath = "//*[@id='account-login']/div[1]"

    def enter_into_login_filed(self):
        self.driver.find_element(By.LINK_TEXT, self.account_link_text).click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, self.log_link_text).click()
        time.sleep(2)

    def enter_to_email_field(self, email):
        self.driver.find_element("id", self.email_field_id).click()
        self.driver.find_element("id", self.email_field_id).send_keys(email)
        time.sleep(2)

    def enter_to_password_field(self, password):
        self.driver.find_element("id", self.password_field_id).click()
        self.driver.find_element("id", self.password_field_id).send_keys(password)
        time.sleep(2)

    def enter_to_login_field(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        time.sleep(2)

    def enter_to_verify(self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_login_link_text).is_displayed()
        time.sleep(2)

    def enter_to_verify_valid_text(self):
        return self.driver.find_element(By.XPATH, self.valid_text_xpath).text
