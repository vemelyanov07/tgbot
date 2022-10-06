from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold, code, italic
from aiogram.utils.emoji import emojize
from aiogram.types import ParseMode, InputMediaPhoto
from config import TOKEN
from .bot import bot, dp


Standart = ""
VIP = ""
VIP_plus = ""

# кальян стандарт
@dp.message_handler(commands=['standart'])
async def proccess_standart_command(message: types.Message):
    caption = "Стандарт"
    await bot.send_photo(message.from_user.id, Standart, caption = caption, reply_to_message_id=message.message_id)

# кальян премиум
@dp.message_handler(commands=['vip'])
async def proccess_vip_command(message: types.Message):
    caption = "Премиум"
    await bot.send_photo(message.from_user.id, VIP, caption = caption, reply_to_message_id=message.message_id)

# кальян премиум плюс(+)
@dp.message_handler(commands=['vipplus'])
async def proccess_vipplus_command(message: types.Message):
    caption = "Премиум +"
    await bot.send_photo(message.from_user.id, VIP_plus, caption = caption, reply_to_message_id=message.message_id)
