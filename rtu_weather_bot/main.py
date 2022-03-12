import asyncio
from aiogram import Bot, Dispatcher, types
import os

BOT_TOKEN = os.environ["RTU_WEATHER_BOT_TOKEN"]


async def start_handler(event: types.Message):
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} 👋!",
        parse_mode=types.ParseMode.HTML,
    )

async def main():
    bot = Bot(token=BOT_TOKEN)
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        await disp.start_polling()
    finally:
        await bot.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
