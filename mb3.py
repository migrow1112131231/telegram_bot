from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = '6702066413:AAGT__eOVNzp9KYehxRp6FD99gxUtRbDQvU'

# создаем объект бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# срабатывает на команду '/help'


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')


@dp.message(Command(commands=['start']))
async def process_start_bot(message: Message):
    await message.answer('Привет!\nЯ эхо-бот\nМожешь написать мне что-нибудь :)')


@dp.message(Command(commands=['contacts']))
async def process_contacts_command(message: Message):
    await message.answer(f'Почтовый ящик: {"boltachev918@gmail.com".rjust(15)}\nvk: {"https://vk.com/m_boltachev".ljust(15)}\ntelegram: @mimiwooo\nНе стесняйся, пиши :)')

@dp.message(F.sticker)
async def send_sticker(message: Message):
    await message.reply_sticker(message.sticker.file_id)
    print('sticker')

@dp.message(F.photo)
async def photo(message: Message):
    await message.answer_photo(message.photo[0].file_id)
    print('photo')

@dp.message(F.document)
async def document(message: Message):
    await message.reply_document(message.document.file_id)
    print('document')

@dp.message(F.voice)
async def process_voice(messsage: Message):
    await messsage.reply_voice(messsage.voice.file_id)
    print('voice')

# срабатывает на любые текстовые сообщения

@dp.message()
async def send_echo(message: Message):
    await message.answer(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)
