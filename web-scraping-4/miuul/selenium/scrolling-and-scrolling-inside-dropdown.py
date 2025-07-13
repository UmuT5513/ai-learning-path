##############################################
# Scrolling and Scrolling Inside Dropdown
##############################################
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.get("https://miuul.com/katalog")
time.sleep(2)

dropdown_button = driver.find_elements(By.XPATH, "//a[@data-bs-toggle='dropdown']")[1]
dropdown_button.click()
time.sleep(0.5)
ul_element = driver.find_elements(By.XPATH, "//ul[@aria-labelledby='navbarDropdown']")[1]
driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", ul_element, "overflow: scroll; height:80px;")

driver.execute_script("arguments[0].focus();", ul_element)
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(0.25)
actions.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(0.25)
actions.send_keys(Keys.ARROW_DOWN).perform()