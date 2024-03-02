import requests
import time

BOT_TOKEN = '6702066413:AAGT__eOVNzp9KYehxRp6FD99gxUtRbDQvU'
BOT_API = 'https://api.telegram.org/bot'
TEXT = 'Спасибо за апдейтик'
ERROR = 'Здесь должна была быть картинка с котиком :('
MAX_COUNTER = 50

offset = -2
counter = 0
cat_link: str
cat_response: requests.Response

while counter < MAX_COUNTER:
    print(counter)
    updates = requests.get(f'{BOT_API}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get('https://api.thecatapi.com/v1/images/search')
            #text = result['message']['text']
            #name = result['message']['from']['first_name']
            if cat_response.status_code == 200:
                #requests.get(f'{BOT_API}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}, {name} :)\nВот твое сообщение:\n{text}\nА теперь лови котика!')
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{BOT_API}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{BOT_API}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR}')

    time.sleep(1)
    counter += 1
