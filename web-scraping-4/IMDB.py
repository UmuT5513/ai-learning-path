from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = webdriver.ChromeOptions()
options.add_argument("--start-minimized")

driver = webdriver.Chrome(options)
driver.get("https://www.imdb.com/list/ls003992425/")
time.sleep(3)


# 
rows = driver.find_elements(By.XPATH, "//ul[contains(@class,'ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM detailed-list-view ipc-metadata-list--base')]/li")
time.sleep(3)

#from selenium.webdriver.support.ui import WebDriverWait
#wait = WebDriverWait(driver, 10)
#rows = wait.until(EC.presence_of_all_elements_located(rows))

names=[]
years=[]
durations=[]
ages=[]
directors=[]

for i,row in enumerate(rows):
    name = row.find_element(By.XPATH, ".//h3")
    infos = row.find_elements(By.XPATH, ".//div[contains(@class,'sc-86fea7d1-7')]/*")
    year,duration,age = infos[0], infos[1], infos[2]
    names.append(name.text), years.append(year.text), durations.append(duration.text), ages.append(age.text)

    # detay sayfasına git yönetmeni al 
    try:
        # h3'ün üstündeki a etiketi
        btn = name.find_element(By.XPATH, "./parent::a")
        btn.click()
        time.sleep(2)
        print("PASS1")
        
        #yönetmen bilgisi 
        # yapı span,div/a'lar(eğer birden fazla director varsa) şeklinde
        ilgili_span = WebDriverWait(driver, 10, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Director')][2]")))
        print("PASS2")

        driver.execute_script("arguments[0].scrollIntoView();", ilgili_span)
        a = ilgili_span.find_elements(By.XPATH, "./following-sibling::div[2]//a")
        director = ", ".join([elem.text for elem in a])                
        
        directors.append(director)
        print(f"Movie {i+1}: {name.text} - Director: {director}")
        print("PASS3")
        #bulduktan sonra geri dön
        driver.back()
        time.sleep(2)
    except Exception as e:
        print(f"Director error for movie {i+1}: {e}")
        director = ""
        directors.append(director)


    try:
        # sayfayı elemntin üzerine getir
        driver.execute_script("arguments[0].scrollIntoView();", row)
    except Exception as e:
        print(f"{e}: {e.__str__}")

    

# csv dosyasına yaz
import pandas as pd
df = pd.DataFrame({'Name': names, 'Year' : years, 'Duration' : durations, 'Age' : ages, 'Director(s)': directors})
df.to_csv('outputs/IMDB_top_10.csv', index=False)
