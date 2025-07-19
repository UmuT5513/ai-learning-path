from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException


def set_up():
    driver = uc.Chrome()
    with driver:
        driver.get("https://orteil.dashnet.org/cookieclicker/")
    time.sleep(1)

    lang = driver.find_element(By.ID,'langSelect-EN')
    lang.click()
    time.sleep(1)

    return driver

def get_elements(driver):
    num = driver.find_element(By.XPATH,'//*[@id="cookies"]')
    num = num.text.split(" ")[0]
    if "," in num:
        num = int(num.replace(",",""))
    per_second = driver.find_element(By.XPATH,'//*[@id="cookiesPerSecond"]')
    
    products_prices = {}
    for i in range(5):
        products_prices[i] = driver.find_element(By.XPATH,f'//*[@id="productPrice{i}"]')
    products_prices = {i: price.text.replace(",","").strip() if "," in price.text else price.text.strip() for i,price in products_prices.items()}

    return num, per_second, products_prices

def main():
    driver = set_up()
    cookie = driver.find_element(By.XPATH,'//*[@id="bigCookie"]')

    start = time.time()
    timeout = start + 60   # 60 seconds from now
    next_update = start + 5
    while time.time() <= timeout:
        cookie.click()

        if time.time() >= next_update:
            num, per_second, product_prices = get_elements(driver=driver)
            print(f"\n[INFO] Cookie sayısı: {num}")
            print(f"[INFO] Ürün fiyatları: {product_prices}")
            affordables = {i: int(price) for i, price in product_prices.items() if price.isdigit() and int(price) <= int(num)}
            print(f"[INFO] Alınabilir ürünler: {affordables}")
            if affordables:
                to_buy = max(affordables, key=affordables.get)
                print(f"[INFO] Satın alınacak ürün indexi: {to_buy}, fiyatı: {affordables[to_buy]}")
                buy_button = driver.find_element(By.ID, f"productPrice{to_buy}")
                if "enabled" in driver.find_element(By.XPATH,"//*[@id='productPrice0']/ancestor::*[2]").get_attribute("class"):
                    print(f"[INFO] Ürün {to_buy} satın alındı!")
                    buy_button.click()
                else:
                    print(f"[INFO] Ürün {to_buy} aktif değil, satın alınamadı.")
            else:
                print("[INFO] Alınabilir ürün yok.")
            print(f"[INFO] --- 5 saniyelik güncelleme tamamlandı ---\n")
            next_update += 5

    print("[INFO] Program sona erdi, tarayıcı kapatılıyor.")
    driver.quit()


if __name__=="__main__":
    main()



    

    
    
