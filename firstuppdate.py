import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6702066413:AAGT__eOVNzp9KYehxRp6FD99gxUtRbDQvU'
TEXT = 'Вау, новый апдейт :)'
MAX_COUNTER:int = 100

offset = -2
chat_id:int

while True:
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            name = result['message']['from']['first_name']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}Спасибо, {name}')

    time.sleep(1)