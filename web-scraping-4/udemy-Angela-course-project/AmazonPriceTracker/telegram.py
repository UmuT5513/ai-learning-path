# chat_id almak için --
#                     |
#                     |
#                     V

import requests
from dotenv import load_dotenv
import os 

load_dotenv()

token = os.getenv('TELEGRAM_TOKEN')
url = f"https://api.telegram.org/bot{token}/getUpdates"
response = requests.get(url)
print(response.json())