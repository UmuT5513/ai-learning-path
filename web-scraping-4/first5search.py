from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options)
driver.get("https://www.google.com/search?q=Araba")
time.sleep(20)

blocks = driver.find_elements(By.XPATH,"//div[contains(@class,'kb0PBd A9Y9g jGGQ5e')]")

dict = {}
searches = []
websites = []
for block in blocks:
    search = block.find_element(By.XPATH,".//h3").text
    website = block.find_element(By.XPATH,".//div[contains(@class,'CA5RN')]//span").text
    searches.append(search)
    websites.append(website)

dict['search_name'] = searches
dict['website_name'] = websites

for key,value in dict.items():
    print(f"{key}: {value}")

