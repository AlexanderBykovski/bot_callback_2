import aiogram
from .buttons_bot import button1, button2

main_keyboard = aiogram.types.ReplyKeyboardMarkup(
    keyboard = [
        [button1, button2]
    ]
    
)