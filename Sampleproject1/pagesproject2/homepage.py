from selenium.webdriver.common.by import *
from Sampleproject1.Locators.Locators import *

class homepage:
    def __init__(self,driver):
        self.driver=driver
        self.about_xpath =Locators.about_xpath
        self.logout_link_text=Locators.logout_link_text

    def click_about(self):
        self.driver.find_element(By.XPATH, self.about_xpath).click()

        # self.driver.find_element(self.about_xpath).click()

    def click_logout(self):
        # self.driver.find_element(self.logout_link_text).click()
        self.driver.find_element(By.LINK_TEXT, self.logout_link_text).click()
