from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F

BOT_TOKEN = '6702066413:AAGT__eOVNzp9KYehxRp6FD99gxUtRbDQvU'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.photo)
async def send_photo(message: Message):
    await message.answer_photo(message.photo[0].file_id)
    print('send photo')

@dp.message(F.audio)
async def send_audio(message: Message):
    await message.answer_audio(message.audio.file_id)
    print('send audio')

@dp.message(F.video)
async def send_video(message: Message):
    await message.answer_video(message.video.file_id)
    print('send video')

@dp.message(F.sticker)
async def send_sticker(message: Message):
    await message.answer_sticker(message.sticker.file_id)
    print('send sticker')

@dp.message(F.animation)
async def send_animation(message: Message):
    await message.answer_animation(message.document.file_id)
    print('send animation')

@dp.message(F.document)
async def send_document(message: Message):
    await message.answer_document(message.document.file_id)
    print('send document')

@dp.message(F.voice)
async def send_voice(message: Message):
    await message.answer_voice(message.voice.file_id)
    print('send voice')

@dp.message(Command(commands=['contacts']))
async def process_contacts_command(message: Message):
    await message.reply(text='Почтовый ящик: boltachev918@gmail.com\nvk: ***\ntelegram: ***')
    print('command contacts')

@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.reply(text='Ура! Стартуем эхо-бот!')
    print('command start')

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.reply(text='Это эхо-бот, отправь мне что-нибудь и получишь это же!')
    print('command help')

@dp.message()
async def reply_message(message: Message):
    await message.answer(text=message.text)
    print('send message')

if __name__ == '__main__':
    dp.run_polling(bot)
