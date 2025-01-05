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
import pytest


class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode (no browser window will pop up)
        chrome_options.add_argument("--disable-extensions")

        chrome_service = Service(chrome_options=chrome_options,executable_path=r'C:\Users\taran\PycharmProjects\pyton2Learning\chromedriver.exe')
        driver = webdriver.Chrome(service=chrome_service)

        driver.implicitly_wait(6)
        driver.maximize_window()
        yield
        print("completed")
        driver.close()

    def test_login(self,test_setup):
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        title1=driver.title
        assert title1 == "OrangeHRM"
        driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()

    # def test_teardown():
    #     print("completed")
    #     driver.close()



