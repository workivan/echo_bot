import os

from aiogram import Bot
from dotenv import load_dotenv

from Storage import Storage

load_dotenv()

API_TOKEN_USER_BOT = os.getenv("USER_BOT_TOKEN")

DB_USER = 'ikuzin'
DB_NAME = 'sound_market'
DB_USER_PASSWORD = 'Pabotahard1$'
DB_URL = f"postgresql://{DB_USER}:{DB_USER_PASSWORD}@localhost:5432/{DB_NAME}"


bot = Bot(token=API_TOKEN_USER_BOT)

storage = Storage()