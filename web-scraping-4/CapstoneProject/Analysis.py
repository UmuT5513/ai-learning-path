from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import html
import pandas as pd

NAMES = []
PRICES = []
DESCRIPTIONS = []
TAXES = []
PRICES_WITH_TAXES = []
AVALIABILITY = []

URL = "https://books.toscrape.com/"

start = time.time()

options = webdriver.ChromeOptions()
options.add_argument("--start-minimized") # küçük ekran
#options.add_argument("--headless") # web sayfasının açılmasında gerek kalmadan işlemler arkaplanda yürür.
driver = webdriver.Chrome(options)
driver.get(URL)
time.sleep(3)

categories = driver.find_elements(By.XPATH, "//ul[contains(@class,'nav')]//ul//a[contains(text(),'Food and Drink') or contains(text(),'Travel')]")


for cat_index in range(len(categories)):
    # her döngüde kategorileri yeniden bul
    categories = driver.find_elements(By.XPATH, "//ul[contains(@class,'nav')]//ul//a[contains(text(),'Food and Drink') or contains(text(),'Travel')]")
    cat = categories[cat_index - 1]
    print(cat.text)
    cat.click()
    time.sleep(2)

    #pagination
    while True:
        books_detay_links = WebDriverWait(driver, 10, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_all_elements_located((By.XPATH, "//img[@class='thumbnail']/parent::a")))

        # sayfanın boş-dolu kontrolü
        if not books_detay_links:
            break

        for book in books_detay_links:
            book.click()
            time.sleep(2)

            source = driver.page_source
            tree = html.fromstring(source)
            #content_div = WebDriverWait(driver, 10, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH, tree(By.XPATH, "//div[@class='content']"))))
            content_div = tree.xpath("//div[@class='content']")[0]
            time.sleep(2)
            content_html = html.tostring(content_div, encoding="unicode")
            soup = BeautifulSoup(content_html, 'html.parser')
            soup.find('article', class_='product-page')

            try:
                book_name = soup.find('h1') # texti alınacak
                book_price = book_name.next_sibling #texti alınacak
                product_desc = soup.find('div', id='product_description').find_next_sibling('p') #texti alınacak
                NAMES.append(book_name.text)
                PRICES.append(book_price.text)
                DESCRIPTIONS.append(product_desc.text)
            except Exception as e:
                print(e)
                NAMES.append("")
                PRICES.append("")
                DESCRIPTIONS.append("")
            
            product_info_table = soup.find('tbody')
            rows = product_info_table.find_all('tr')
            try:
                for row in rows:
                    th = row.find('th')
                    if th.text == 'Tax':
                        Tax = th.find_next_sibling('td').text
                        TAXES.append(Tax)
                    if "excl" in th.text:
                        price_tax = th.find_next_sibling('td').text
                        PRICES_WITH_TAXES.append(price_tax)
                    if th.text == 'Availability':
                        avaliability = th.find_next_sibling('td').text
                        AVALIABILITY.append(avaliability)
            except Exception as e:
                print(e)
                TAXES.append("")
                PRICES_WITH_TAXES.append("")
                AVALIABILITY.append("")
    
            driver.back()
            time.sleep(2)

        # sonraki sayfa var mı?
        try:
            next_btn = driver.find_element(By.XPATH, "//li[@class='next']/a")
            next_btn.click()
            time.sleep(2)
            print("PASS2")
        except:
            print("İşlem Tamamlandı!")
            break
end = time.time()
print(end - start)
driver.quit()

dict = {
    'name': NAMES,
    'price': PRICES,
    'description': DESCRIPTIONS,
    'tax': TAXES,
    'price_with_tax': PRICES_WITH_TAXES,
    'avalibility': AVALIABILITY}

print(len(NAMES))
print(len(PRICES))
print(len(DESCRIPTIONS))
print(len(TAXES))
print(len(PRICES_WITH_TAXES))
print(len(AVALIABILITY))

try:
    pd.DataFrame(dict).to_csv('outputs/miuul_capstone.csv', index=False)
except Exception as e:
    print(e)
    # After scraping each book (inside the for book in books_detay_links loop)
    if len(NAMES) != len(PRICES) or len(NAMES) != len(DESCRIPTIONS) or len(NAMES) != len(TAXES) or len(NAMES) != len(PRICES_WITH_TAXES) or len(NAMES) != len(AVALIABILITY):
        # Fill missing values with empty strings
        max_len = max(len(NAMES), len(PRICES), len(DESCRIPTIONS), len(TAXES), len(PRICES_WITH_TAXES), len(AVALIABILITY))
        for lst in [NAMES, PRICES, DESCRIPTIONS, TAXES, PRICES_WITH_TAXES, AVALIABILITY]:
            while len(lst) < max_len:
                lst.append("")
    pd.DataFrame(dict).to_csv('C:/Users/Umut/Desktop/ai-learning-path/web-scraping-4/outputs/miuul_webscraping_capstone.csv', index=False)




