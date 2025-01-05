import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import unittest
from Sampleproject1.pagesproject2.homepage import *
from Sampleproject1.pagesproject2.loginpage import *
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))

class login2(unittest.TestCase):
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
        driver=self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        login2 = loginpage(driver)
        login2.enter_username("Admin")
        login2.enter_password("admin123")
        login2.click_login()

        homepage2=homepage(driver)
        homepage2.click_about()
        homepage2.click_logout()
        time.sleep(3)
        # self.driver.find_element(By.NAME, "username").send_keys("Admin")
        # self.driver.find_element(By.NAME, "password").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        # self.driver.find_element(By.LINK_TEXT, "Logout").click()
        # time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print ("completed")

if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner
    (output=r'C:\Users\taran\PycharmProjects\pyton2Learning\Htmproject1report'),verbosity=2)

