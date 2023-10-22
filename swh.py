import os
import requests

from dotenv import load_dotenv

load_dotenv()

TG_API_KEY = os.getenv('BOT_API_KEY')
whook = 'https://b2b6f4590680b0.lhr.life'

r = requests.get(f'https://api.telegram.org/bot{TG_API_KEY}/setWebhook?url={whook}/')

print(r.json())
