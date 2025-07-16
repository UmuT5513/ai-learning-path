from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://books.toscrape.com/"

options = webdriver.ChromeOptions()
options.add_argument("--start-minimized") # küçük ekran
#options.add_argument("--headless") # web sayfasının açılmasında gerek kalmadan işlemler arkaplanda yürür.
driver = webdriver.Chrome(options)
driver.get(URL)
time.sleep(3)

categories = driver.find_elements(By.XPATH, "//ul[contains(@class,'nav')]//ul//a[contains(text(),'Nonfiction') or contains(text(),'Travel')]")
print(categories)



travel = categories[0]
travel.click()
print("PASS1")
books_detay_links = WebDriverWait(driver, 10, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_all_elements_located((By.XPATH, "//img[@class='thumbnail']")))
print("PASS2")

print(books_detay_links[0].get_attribute("alt"))


