import time

import selenium
from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
import unittest

class login1(unittest.TestCase):
    #run before class setup only once
    @classmethod
    def setUpClass(cls):
        cls.chrome_options = Options()
        cls.chrome_service = Service(chrome_options=cls.chrome_options,
        executable_path=r'C:\Users\taran\PycharmProjects\pyton2Learning\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=cls.chrome_service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print ("completed")

if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner
    (output=r'C:\Users\taran\PycharmProjects\pyton2Learning\Htmproject1report'),verbosity=3)


