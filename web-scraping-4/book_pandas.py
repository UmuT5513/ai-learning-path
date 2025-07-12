import requests
from bs4 import BeautifulSoup

result = requests.get("https://books.toscrape.com/")
if result.status_code == 200:
    html = result.content
    soup = BeautifulSoup(html, 'html.parser')
    print('Çorba Malzemeleri Eklendi Kaynatılmaya Hazır!')

dict = {}


books = soup.find('section').find_all('div')[1].find('ol').find_all('article')
names=[]
prices=[]
in_stocks=[]

for book in books:
    name = book.find('h3').find('a').text
    
    product_price = book.find('div', attrs={'class':'product_price'}).find_all('p')
   
    price = product_price[0].text
    try:
        price_float = float(price.replace('£',''))
    except Exception as e:
        print(f"{e} : {e.__str__}")

    in_stock = False
    stock = product_price[1].text.strip()
    if stock == "In stock":
        in_stock = True
    else:
        continue

    print(f"{name}: {price}\nStokta var mı: {'✅' if in_stock==True else '❌'}")

    names.append(name)
    prices.append(price_float)
    in_stocks.append(in_stock)

dict['name'] = names
dict['price'] = prices
dict['stock'] = in_stocks

try:
    import pandas as pd
    df = pd.DataFrame.from_dict(dict,orient='columns')
    df.to_csv('outputs/books.csv')
except Exception as e:
    print(f"{e} : {e.__str__}")

df = pd.read_csv('outputs/books.csv')
print(df)
