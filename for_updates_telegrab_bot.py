from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN = '6702066413:AAGT__eOVNzp9KYehxRp6FD99gxUtRbDQvU'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def analyze_update(message: Message):
    print(message.model_dump_json(indent=5, exclude_none=True))

if __name__ == '__main__':
    dp.run_polling(bot)