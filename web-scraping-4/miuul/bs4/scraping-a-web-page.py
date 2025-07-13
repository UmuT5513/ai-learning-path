#######################################
# Scraping a Web Page
#######################################
# pip install requests
import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.example.com")
result.status_code
html = result.content
soup = BeautifulSoup(html, "html.parser")
soup.find("h1").text
