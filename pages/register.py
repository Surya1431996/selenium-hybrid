from selenium.webdriver.common.by import By
import time


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    account_link_text = "My Account"
    reg_link_text = "Register"
    first_field_id = "input-firstname"
    last_field_id = "input-lastname"
    emai_field_id = "input-email"
    tel_field_id = "input-telephone"
    pas_field_id = "input-password"
    cpas_field_id = "input-confirm"
    rad_button_xpath = "//*[@id='content']/form/fieldset[3]/div/div/label[1]/input"
    ag_field_name = "agree"
    lo_button_xpath = "//*[@id='content']/form/div/div/input[2]"
    cre_msg_xpath = "//*[@id='content']/h1"
    dp_msg_xpath = "//*[@id='account-register']/div[1]"
    pp_msg_xpath = "//*[@id='account-register']/div[1]"
    ffn_msg_xpath = "//*[@id='account']/div[2]/div/div"
    ln_msg_xpath = "//*[@id='account']/div[3]/div/div"
    em_msg_xpath = "//*[@id='account']/div[4]/div/div"
    te_msg_xpath = "//*[@id='account']/div[5]/div/div"
    ps_msg_xpath = "//*[@id='content']/form/fieldset[2]/div[1]/div/div"

    def enter_into_reg_filed(self):
        self.driver.find_element(By.LINK_TEXT, self.account_link_text).click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, self.reg_link_text).click()
        time.sleep(2)

    def enter_into_reg_fn(self, firstname):
        self.driver.find_element("id", self.first_field_id).click()
        self.driver.find_element("id", self.first_field_id).send_keys(firstname)
        time.sleep(2)

    def enter_into_reg_ln(self, lastname):
        self.driver.find_element("id", self.last_field_id).click()
        self.driver.find_element("id", self.last_field_id).send_keys(lastname)
        time.sleep(2)

    def enter_into_reg_em(self, email):
        self.driver.find_element("id", self.emai_field_id).click()
        self.driver.find_element("id", self.emai_field_id).send_keys(email)
        time.sleep(2)

    def enter_into_reg_appl(self, telephonenumber):
        self.driver.find_element("id", self.tel_field_id).click()
        self.driver.find_element("id", self.tel_field_id).send_keys(telephonenumber)
        time.sleep(2)

    def enter_into_reg_pas(self, password):
        self.driver.find_element("id", self.pas_field_id).click()
        self.driver.find_element("id", self.pas_field_id).send_keys(password)
        time.sleep(2)

    def enter_into_reg_cpas(self, cpassword):
        self.driver.find_element("id", self.cpas_field_id).click()
        self.driver.find_element("id", self.cpas_field_id).send_keys(cpassword)
        time.sleep(2)

    def enter_radio_but(self):
        self.driver.find_element(By.XPATH, self.rad_button_xpath).click()
        time.sleep(2)

    def enter_into_reg_ag(self):
        self.driver.find_element(By.NAME, self.ag_field_name).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.lo_button_xpath).click()
        time.sleep(2)

    def account_created(self):
        return self.driver.find_element(By.XPATH, self.cre_msg_xpath).text

    def dup_email(self):
        return self.driver.find_element(By.XPATH, self.dp_msg_xpath).text

    def dup_pp(self):
        return self.driver.find_element(By.XPATH, self.pp_msg_xpath).text

    def dup_fn(self):
        return self.driver.find_element(By.XPATH, self.ffn_msg_xpath).text

    def dup_ln(self):
        return self.driver.find_element(By.XPATH, self.ln_msg_xpath).text

    def dup_ema(self):
        return self.driver.find_element(By.XPATH, self.em_msg_xpath).text

    def dup_tele(self):
        return self.driver.find_element(By.XPATH, self.te_msg_xpath).text

    def dup_pwd(self):
        return self.driver.find_element(By.XPATH, self.ps_msg_xpath).text


