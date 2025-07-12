import requests
from parsel import Selector

# 1. Hedef URL
url = 'https://quotes.toscrape.com/'

# 2. HTTP isteği gönder
response = requests.get(url)

# 3. Yanıtı parse et
sel = Selector(text=response.text)

authortext_xpath = "//div[contains(@class,'quote')]/span[contains(@class,'text')]/text()"
text_xpath = "//small[contains(@class,'author')]/text()"


for author, text in zip(sel.xpath(text_xpath), sel.xpath(authortext_xpath)): # zip combine two lists element by element.
    print(f"{author.get().strip()} - {text.get().strip()}")