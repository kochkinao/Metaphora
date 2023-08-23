from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config

storage = MemoryStorage()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot=bot, storage=storage)