from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

chrome_driver_path = ChromeDriverManager().install()
# firefoxd=GeckoDriverManager().install()
options = Options()
service = Service(chrome_driver_path)

# driver = webdriver.Firefox(service=service, options=options)



driver = webdriver.Chrome(service=service)
# driver2=webdriver.Firefox(service=service1)

# driver = webdriver_manager.chrome(ChromeDriverManager().install())
# driver2 = webdriver.firefox(GeckoDriverManager().install())
# driver3 = webdriver.ie(IEDriverManager().install())

driver.get("https://google.com")
driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('automation step by step')
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(keys.Keys.RETURN)
time.sleep(10)

print(driver.title)
time.sleep(4)

driver.close()
driver.quit