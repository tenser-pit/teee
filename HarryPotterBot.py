from aiogram import Bot, types, Dispatcher, executor

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(Bot)

# @dp.message_handler()
# async def


if __name__ == '__main__':
    executor.start_polling(dp)