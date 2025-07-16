from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--start-minimized")

driver = webdriver.Chrome(options)
driver.get("https://www.imdb.com/list/ls003992425/")
time.sleep(3)

# Wait for elements to load
wait = WebDriverWait(driver, 10)

rows = driver.find_elements(By.XPATH, "//ul[contains(@class,'ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM detailed-list-view ipc-metadata-list--base')]/li")
time.sleep(3)

names = []
years = []
durations = []
ages = []
directors = []

for i in range(len(rows)):
    # Re-find elements to avoid stale element references
    rows = driver.find_elements(By.XPATH, "//ul[contains(@class,'ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM detailed-list-view ipc-metadata-list--base')]/li")
    row = rows[i]

    name = row.find_element(By.XPATH, ".//h3")
    infos = row.find_elements(By.XPATH, ".//div[contains(@class,'sc-86fea7d1-7')]/*")
    year, duration, age = infos[0], infos[1], infos[2]
    names.append(name.text)
    years.append(year.text)
    durations.append(duration.text)
    ages.append(age.text)

    # Navigate to detail page to get director
    try:
        # Click on the movie title link
        btn = name.find_element(By.XPATH, "./parent::a")
        btn.click()
        
        # Wait for page to load
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        
        # Find director information - try multiple selectors
        director = ""
        try:
            # Method 1: Look for Directors section in the main cast/crew area
            director_elements = driver.find_elements(By.XPATH, "//li[@data-testid='title-pc-principal-credit' and .//span[contains(text(), 'Director')]]//a")
            if director_elements:
                director = ", ".join([elem.text for elem in director_elements])
            else:
                # Method 2: Try alternative selector
                director_elements = driver.find_elements(By.XPATH, "//span[text()='Director' or text()='Directors']/following-sibling::div//a | //span[text()='Director' or text()='Directors']/parent::*/following-sibling::div//a")
                if director_elements:
                    director = ", ".join([elem.text for elem in director_elements])
                else:
                    # Method 3: Try in the cast section
                    director_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/name/') and contains(following-sibling::text(), 'Director')]")
                    if director_elements:
                        director = ", ".join([elem.text for elem in director_elements])
        except Exception as e:
            print(f"Error finding director: {e}")
            director = ""
        
        directors.append(director)
        print(f"Movie {i+1}: {name.text} - Director: {director}")
        
        # Go back to list page
        driver.back()
        
        # Wait for the list page to load again
        wait.until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class,'ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM detailed-list-view ipc-metadata-list--base')]/li")))
        
    except Exception as e:
        print(f"Director error for movie {i+1}: {e}")
        directors.append("")
        # If we're not on the list page, try to go back
        if "list" not in driver.current_url:
            driver.back()
            time.sleep(2)

    # Scroll to next element
    try:
        if i < len(rows) - 1:
            next_rows = driver.find_elements(By.XPATH, "//ul[contains(@class,'ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM detailed-list-view ipc-metadata-list--base')]/li")
            if i + 1 < len(next_rows):
                driver.execute_script("arguments[0].scrollIntoView();", next_rows[i + 1])
    except Exception as e:
        print(f"Scroll error: {e}")

driver.quit()

# Create DataFrame and save to CSV
df = pd.DataFrame({
    'Name': names, 
    'Year': years, 
    'Duration': durations, 
    'Age': ages, 
    'Director(s)': directors
})

df.to_csv('outputs/claude_IMDB_top_10.csv', index=False)
print("Scraping completed successfully!")
print(df)