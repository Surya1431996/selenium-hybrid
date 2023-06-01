from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from utilities.customlogger import LogGen
from pages.register import RegisterPage


@pytest.mark.usefixtures("setup")
class Testregister:
    logger = LogGen.Loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_for_mandatory_fields(self):
        self.logger.info("*****************Testregister mandatory fileds started****************************")
        self.logger.info("*****************input all values started****************************")
        registerpage = RegisterPage(self.driver)
        registerpage.enter_into_reg_filed()
        registerpage.enter_into_reg_fn("surya")
        registerpage.enter_into_reg_ln("teja")
        registerpage.enter_into_reg_em("teja12345@gmail.com")
        registerpage.enter_into_reg_appl("1234567")
        registerpage.enter_into_reg_pas("12345678")
        registerpage.enter_into_reg_cpas("12345678")
        registerpage.enter_into_reg_ag()
        sucmsg = "Your Account Has Been Created!"
        assert registerpage.account_created().__contains__(sucmsg)
        self.logger.info("*****************Account is created****************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_for_all_fields(self):
        self.logger.info("*****************Testregister all fields started****************************")
        self.logger.info("*****************input all values  started****************************")
        registerpage = RegisterPage(self.driver)
        registerpage.enter_into_reg_filed()
        registerpage.enter_into_reg_fn("surya")
        registerpage.enter_into_reg_ln("teja")
        registerpage.enter_into_reg_em("teja1234567@gmail.com")
        registerpage.enter_into_reg_appl("1234567")
        registerpage.enter_into_reg_pas("12345678")
        registerpage.enter_into_reg_cpas("12345678")
        registerpage.enter_radio_but()
        registerpage.enter_into_reg_ag()
        succmsg = "Your Account Has Been Created!"
        assert registerpage.account_created().__contains__(succmsg)
        self.logger.info("*****************Testregister account created ****************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_for_duplicate_email(self):
        self.logger.info("*****************Dupicate email test started****************************")
        registerpage = RegisterPage(self.driver)
        registerpage.enter_into_reg_filed()
        registerpage.enter_into_reg_fn("surya")
        registerpage.enter_into_reg_ln("teja")
        registerpage.enter_into_reg_em("teja1234567@gmail.com")
        registerpage.enter_into_reg_appl("1234567")
        registerpage.enter_into_reg_pas("12345678")
        registerpage.enter_into_reg_cpas("12345678")
        registerpage.enter_radio_but()
        registerpage.enter_into_reg_ag()
        wamsg = "Warning: E-Mail Address is already registered!"
        assert registerpage.dup_email().__contains__(wamsg)
        self.logger.info("*****************Registration not completed due to duplicate email ****************************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_for_empty_fileds(self):
        self.logger.info("*****************Registiration page Empty Fields test started****************************")
        registerpage = RegisterPage(self.driver)
        registerpage.enter_into_reg_filed()
        registerpage.enter_into_reg_fn(" ")
        registerpage.enter_into_reg_ln(" ")
        registerpage.enter_into_reg_em(" ")
        registerpage.enter_into_reg_appl(" ")
        registerpage.enter_into_reg_pas(" ")
        registerpage.enter_into_reg_cpas(" ")
        registerpage.enter_radio_but()
        registerpage.enter_into_reg_ag()
        time.sleep(2)

        warn2msg = "First Name must be between 1 and 32 characters!"
        assert registerpage.dup_fn().__contains__(warn2msg)
        self.logger.info("*****************First name box empty****************************")
        warn3msg = "Last Name must be between 1 and 32 characters!"
        assert registerpage.dup_ln().__contains__(warn3msg)
        self.logger.info("*****************Last name box empty****************************")
        warn4msg = "E-Mail Address does not appear to be valid!"
        assert registerpage.dup_ema().__contains__(warn4msg)
        self.logger.info("*****************Email box empty****************************")
        warn5msg = "Telephone must be between 3 and 32 characters!"
        assert registerpage.dup_tele().__contains__(warn5msg)
        self.logger.info("*****************Telephone box empty****************************")
        warn6msg = "Password must be between 4 and 20 characters!"
        assert registerpage.dup_pwd().__contains__(warn6msg)
        self.logger.info("*****************Password box empty****************************")
        self.logger.info("*****************Registration Page Testing Completed****************************")

