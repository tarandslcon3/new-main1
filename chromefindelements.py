import time

import selenium
from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
# from selenium.webdriver.common import by
from selenium.webdriver.common.by import *
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no browser window will pop up)
chrome_options.add_argument("--disable-extensions")

chrome_service = Service(chrome_options=chrome_options,executable_path=r'C:\Users\taran\PycharmProjects\pyton2Learning\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service)

driver.set_page_load_timeout(10)

driver.get("https://google.com")
WebDriverWait(driver, 10)

driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('automation step by step')
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(keys.Keys.RETURN)
time.sleep(10)

print(driver.title)
