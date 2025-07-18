from bs4 import BeautifulSoup
import requests
import schedule
import time
import datetime



def scrape_product_infos(soup):
    center_col = soup.find('div', id='centerCol')
    if not center_col:
        print("centerCol bulunamadı!")
        return None
    apex = center_col.find('div', id='apex_desktop')
    if not apex:
        print("apex_desktop bulunamadı!")
        return None
    whole = apex.find(class_='a-price-whole')
    fraction = apex.find(class_='a-price-fraction')
    price_text = f"{whole.text}{fraction.text}TL"
    price = float(price_text.replace("TL","").replace(",","."))

    title = soup.find(id='productTitle').get_text().strip()
    return price, title
    

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    r = requests.post(url, data=payload)
    return r.json()




def main():
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
          'Accept-Language':'tr-TR,tr;q=0.5'}

    URL = "https://www.amazon.com.tr/HP-D%C3%B6n%C3%BC%C5%9F%C3%BCml%C3%BC-Polyester-Ge%C3%A7irmez-%C3%87%C4%B1kar%C4%B1labilir/dp/B0DCK3KTG5/?_encoding=UTF8&ref_=pd_hp_d_btf_ci_mcx_mr_ca_id_hp_d"
    response = requests.get(URL, headers=header)
    soup = BeautifulSoup(response.content, "html.parser")

    price, title = scrape_product_infos(soup=soup)

    th_price = 600

    if price < th_price:
        #send telegram message
        
        token = "7890217994:AAHD-8Q8BCknBLC-86gg7m2vojoYgEfsSgk"
        chat_id = "1270406331"
        message = f"{title} ürünü *{price} TL* fiyatına düştü! ({datetime.datetime.now().strftime('%Y-%m-%d')})"
        send_telegram_message(token=token, chat_id=chat_id, message=message)
        print("mesaj gönderildi")


if __name__ == "__main__":
    main()
    




#schedule.every().day.at("15:40").do(send_message)
#while True:
#    schedule.run_pending()
#    time.sleep(60)