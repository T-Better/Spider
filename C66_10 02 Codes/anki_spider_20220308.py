import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

p1 = r'D:\Program Files\pagetest\注册A.html'

driver = webdriver.Chrome()
driver.get(p1)
"""
e1 = driver.find_element(By.XPATH,'//p/button')
action = ActionChains(driver)
action.move_to_element(e1).perform()
time.sleep(2)
"""
action = ActionChains(driver)
e2 = driver.find_element(By.CSS_SELECTOR,'')
action.context_click(e2).perform()

driver.close()
