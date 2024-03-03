import requests
import time

BOT_API = 'https://api.telegram.org/bot'
BOT_TOKEN = '6702066413:AAGT__eOVNzp9KYehxRp6FD99gxUtRbDQvU'

offset = -2
timeout = 20.63


def text() -> None:
    print('Был апдейтик :)')


while True:
    start_time = time.time()
    updates = requests.get(
        f'{BOT_API}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for element in updates['result']:
            text()
            first_name = element['message']['from']['first_name']
            chat_id = element['message']['chat']['id']
            offset = element['update_id']

            requests.get(
                f'{BOT_API}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={first_name}. Спасибо за апдейтик :)')

    print(time.time() - start_time)
