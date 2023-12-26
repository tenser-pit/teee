from aiogram import Dispatcher, executor, types, Bot

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот был запущен')


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('<b>Привет,</b> <em>Добро пожаловать</em>', parse_mode='HTML')


    


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
