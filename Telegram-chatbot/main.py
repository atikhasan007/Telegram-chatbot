import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from google import genai

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_KEY = os.getenv("GMINAI_API_KEY")

logging.basicConfig(level=logging.INFO)

client = genai.Client(api_key=API_KEY)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

conversation = {}

@dp.message_handler(commands=['start'])
async def start(m: types.Message):
    await m.reply("Hello! I am your Gemini chat bot. Created by Atik 👋")

@dp.message_handler()
async def chat(m: types.Message):
    try:
        user_id = m.from_user.id
        if user_id not in conversation:
            conversation[user_id] = client.chats.create(model="gemini-2.5-flash")
        chat_session = conversation[user_id]

        response = chat_session.send_message(m.text)
        await m.reply(response.text)

    except Exception as e:
        await m.reply(f"Error: {e}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
