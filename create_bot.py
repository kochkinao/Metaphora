from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bd import Database
import config

storage = MemoryStorage()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

db = Database('save_message.db')