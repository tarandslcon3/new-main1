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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common import by

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no browser window will pop up)
chrome_options.add_argument("--disable-extensions")

chrome_service = Service(chrome_options=chrome_options,executable_path=r'C:\Users\taran\PycharmProjects\pyton2Learning\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service)
#implicit wait for entire section
# driver.implicitly_wait(20.4)

driver.get("https://google.com")




driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('automation step by step')
# driver.find_element(By.NAME,'btnK').send_keys(keys.Keys.RETURN)
wait1=WebDriverWait(driver,10)
try:
    element =wait1.until(ec.element_to_be_clickable((By.NAME, 'btnK1')))
    print("element found")
except:
    print("element not found")
    exit (1)
element.click()

# driver.find_element(By.NAME,'btnK').click()




print(driver.title)
print ("test completed")