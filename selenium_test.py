from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


chromedriver = "/chromedriver"
option = webdriver.ChromeOptions()
s = Service(chromedriver)

driver = webdriver.Chrome(service=s, options=option)

driver.get("https://simplyhired.com")
search = driver.find_element(By.NAME,"q")
search.send_keys("Machine Learning")
search.send_keys(Keys.RETURN)

job_list = driver.find_element(By.ID,"job-list")
for job in job_list:   
    print(job_list)
    
driver.quit()
