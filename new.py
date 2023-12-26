from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

HELP_COMMAND = """
/help - список команд
/start - Начать работу с ботом
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text='Добро пожаловать')
    await message.delete()


if __name__ == '__main__':
    # skip_updates - True: не отвечает на сообщения после включения бота
    executor.start_polling(dp, skip_updates=True)