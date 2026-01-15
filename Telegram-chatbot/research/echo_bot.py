import logging
from google import genai
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or `/help` command
    """
    await message.reply("Hi\nI am Echo Bot!\nPowered By Atik")



    #create echo function
    @dp.message_handler()
    async def echo(message: types.Message):
        """
        This will  return echo

        """
        await message.answer(message.text)

        


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
