from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import *
import HtmlTestRunner
import unittest


class googlesearch(unittest.TestCase):
    #run before class setup only once
    @classmethod
    def setUpClass(cls):
        cls.chrome_options = Options()
        cls.chrome_service = Service(chrome_options=cls.chrome_options,
        executable_path=r'C:\Users\taran\PycharmProjects\pyton2Learning\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=cls.chrome_service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def testSearchgoogle(self):
        self.driver.get('https://google.com')
        self.driver.find_element(By.NAME, "q").send_keys("Automation")
        self.driver.find_element(By.NAME, 'btnI').click()
        print(self.driver.title)


#test
    @classmethod
    def tearDownClass(cls):
        print('test completed')
        cls.driver.close()

if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\taran\PycharmProjects\pyton2Learning\Htmproject1report'),verbosity=2)





