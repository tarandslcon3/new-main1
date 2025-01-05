from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import *
from Sampleproject1.Locators.Locators import *
class loginpage:
    def __init__(self,driver):
        self.driver=driver
        self.username_text_box_name=Locators.username_text_box_name
        self.password_name=Locators.password_name
        self.login_button_xpath=Locators.login_button_xpath

    def enter_username(self,username):
        # self.driver.find_element(self.username_text_box_name).clear()
        self.driver.find_element(By.NAME, self.username_text_box_name).send_keys(username)
        # self.driver.find_element(self.username_text_box_name).send_keys(username)

    def enter_password(self,password):
        # self.driver.find_element(self.password_name).clear()
        self.driver.find_element(By.NAME, self.password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()


