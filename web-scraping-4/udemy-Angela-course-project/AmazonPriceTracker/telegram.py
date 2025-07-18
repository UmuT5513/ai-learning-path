# chat_id almak için --
#                     |
#                     |
#                     V

import requests

token = "7890217994:AAHD-8Q8BCknBLC-86gg7m2vojoYgEfsSgk"
url = f"https://api.telegram.org/bot{token}/getUpdates"
response = requests.get(url)
print(response.json())