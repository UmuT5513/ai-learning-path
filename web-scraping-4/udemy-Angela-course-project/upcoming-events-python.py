from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://www.python.org/")

table = driver.find_element(By.CLASS_NAME,'shrubbery')
rows = table.find_elements(By.TAG_NAME,'li')
inner_dict = {}
outter_dict = {}
for i,row in enumerate(rows):
    time = row.find_element(By.TAG_NAME,'time').text
    event = row.find_element(By.TAG_NAME,'a').text
    inner_dict['time'] = time
    inner_dict['name'] = event
    outter_dict[i] = inner_dict
print("Başaılı!")
print(outter_dict)