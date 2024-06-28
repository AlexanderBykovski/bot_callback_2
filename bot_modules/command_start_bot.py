from .dispatcher_bot import dispatcher
from .keyboards_bot import main_keyboard 
import aiogram
import aiogram.filters

@dispatcher.message(aiogram.filters.CommandStart())
async def bot_start(message: aiogram.types.Message):
    await message.answer(text = "Hello, User!", reply_markup = main_keyboard)