import requests
from parsel import Selector

# 1. Hedef URL
url = 'https://books.toscrape.com/'

# 2. HTTP isteği gönder
response = requests.get(url)

# 3. Yanıtı parse et
sel = Selector(text=response.text)

book_container = "//article" # it contains image, name, price, start rating
filtered_books = []

for book in sel.xpath(book_container):
    name = book.xpath("h3/a/text()").get()
    try:
        price_text = book.xpath("div[last()]/p[1]/text()").get().replace("Â£", "").strip()
        price = float(price_text)
    except Exception as e:
        print(f"Hata: {e} - {name}")
        continue

    if price > 20:
        filtered_books.append(book)
        print(f"{name} kitabı {price} TL'de satılıyor. filtered_books listesine eklendi.")

print(len(filtered_books))




    