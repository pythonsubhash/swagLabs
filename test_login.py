import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


class Test_001_Login:
    base_url= "https://www.saucedemo.com/"
    username= "standard_user"
    password = "secret_sauce"
    logger = LogGen.loggen()

# validation of home page ,this one test case
    def test_hmoePageTitle(self,setup):
        self.logger.info("******Test_001_Login*******")
        self.logger.info("******* verifying homepage title *******")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        if act_title== "Swag Labs":
            assert True
            self.logger.info("******* homepage title passed *******")

            self.driver.close()


        else:
            self.driver.save_screenshot("Screenshots\\hompage.png")
            self.driver.close()
            self.logger.error("******* hompage title failed *******")

            assert False

# login page validation 2nd test case
    def test_login(self,setup):
        self.logger.info("******* verifying logintest *******")

        self.driver = setup
        self.driver.get(self.base_url)
# to access LoginPage class we have to create opject for that class
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # validation succesful login
        act_title=self.driver.title
        if act_title == "Swag Labs":
            assert True
            self.logger.info("******* login test passed *******")

            self.driver.close()

        else:
            self.driver.save_screenshot("Screenshots\\login.png")
            self.logger.error("******* login test failed *******")

            assert False





