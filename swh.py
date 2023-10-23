import os
import requests

from dotenv import load_dotenv

load_dotenv()

TG_API_KEY = os.getenv('BOT_API_KEY')
whook = 'https://38ca3eeff94f28.lhr.life'

r = requests.get(f'https://api.telegram.org/bot{TG_API_KEY}/setWebhook?url={whook}/')

print(r.json())
