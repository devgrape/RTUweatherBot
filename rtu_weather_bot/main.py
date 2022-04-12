import asyncio
from aiogram import Bot, Dispatcher, types, executor
import os

BOT_TOKEN = os.environ["RTU_WEATHER_BOT_TOKEN"]
bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "restart"])
async def start_handler(event: types.Message):
    """ Функция, которая приветствует пользователя после команд /start и /restart"""

    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} 👋!",
        parse_mode=types.ParseMode.HTML,
    )

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    """ Функция, которая выдает вспомогательную информацию для работы с ботом"""

    await message.reply("Вспомогательная информация")



if __name__ == '__main__':
    #asyncio.get_event_loop().run_until_complete(main())
    executor.start_polling(dp)
