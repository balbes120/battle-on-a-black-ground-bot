import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = os.getenv("TOKEN")
WEBHOOK_HOST = 'https://' + os.getenv("WEBHOOK_HOST")
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# 📌 Команда /start для регистрации
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer(f" Привет, {message.from_user.first_name}!\n"
                         f"Ты попал в темную землю.\n"
                         f"Напиши /create, чтобы создать своего война.")

# 📌 Команда /create (создание война)
@dp.message_handler(commands=['create'])
async def create_warrior(message: types.Message):
    warriors = ["Мелкий", "Некитос", "Апсалутик", "Илюша"]
    from random import choice
    warrior = choice(warriors)
    await message.answer(f"ты стал: {warrior}")

# 🔧 Запуск webhook
async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    await bot.delete_webhook()

if __name__ == '__main__':
    from aiogram import executor
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host="0.0.0.0",
        port=int(os.environ.get('PORT', 5000)),
    )