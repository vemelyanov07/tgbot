from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text, code, italic
from aiogram.types import ParseMode
from aiogram.types.message import ContentType
from sqlalchemy import func
from config import TOKEN
from kb import Standart_keyboard, Delivery, inline_keyboard1,\
            taste_keyboard, time_of_deliveo, inline_keyboard2,\
             inline_keyboard3, inline_keyboard4


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#начало работы с ботом(выбор кальянов)
@dp.message_handler(commands=['start'])
async def proccess_start_command(message: types.Message):
    await message.reply("Доброго времени суток! Выберите вид кальяна ⚖️", reply_markup=Standart_keyboard)
    await bot.send_photo(message.from_user.id, photo=open('static\hookah.jpg', 'rb'))

#выбор вкуса кальяна
@dp.message_handler(commands=['taste'])
async def proccess_taste_command(message: types.Message):
    await message.reply("Выберите вкус кальяна 💎", reply_markup=taste_keyboard)

#время доставки
@dp.message_handler(commands=['time'])
async def proccess_time_command(message: types.Message):
    await message.reply("Выберите время для доставки 🎁", reply_markup=time_of_deliveo)

#доставка
@dp.message_handler(commands=['delivery'])
async def proccess_delivery_command(message: types.Message):
    await message.reply("Данные для доставки 📜", reply_markup=Delivery)

# спасибо за заказ
@dp.message_handler(commands=['thank'])
async def proccess_thank_command(message: types.Message):
    await message.answer("Спасибо. Ваш заказ принят. Менеджер свяжется с Вами в ближайшее время.")

#доступный выбор действия
@dp.message_handler(commands=['help'])
async def proccess_help_command(message: types.Message):
    await message.reply("Выберите вид кальяна 🔥",
                        reply_markup=inline_keyboard1) 
    await message.reply("Выберите вкус кальяна 🔥",
                        reply_markup=inline_keyboard2) 
    await message.reply("Данные для доставки 🔥",
                        reply_markup=inline_keyboard3)
    await message.reply("Выберите время для доставки 🔥",
                        reply_markup=inline_keyboard4)


@dp.message_handler()
async def hookah_taste(message: types.Message):
    if message.text == "Стандарт ✈️":
        await bot.send_photo(message.from_user.id, photo=open('static\standart.jpg', 'rb'))
        await message.answer("Выберите вкус кальяна 💎", reply_markup=taste_keyboard)
    if message.text == "Премиум 🚀":
        await bot.send_photo(message.from_user.id, photo=open('static\premium.jpg', 'rb'))
        await message.answer("Выберите вкус кальяна 💎", reply_markup=taste_keyboard)
    if message.text == "Премиум + 🛸":
        await bot.send_photo(message.from_user.id, photo=open('static\premium_plus.jpg', 'rb'))
        await message.answer("Выберите вкус кальяна 💎", reply_markup=taste_keyboard)
    if message.text == "Свежий 🧊🌱":
        await message.answer("Выберите время для доставки 🎁", reply_markup=time_of_deliveo)
    if message.text == "Кислый 🍋🍇":
        await message.answer("Выберите время для доставки 🎁", reply_markup=time_of_deliveo)
    if message.text == "Сладкий 🥝🥭":
        await message.answer("Выберите время для доставки 🎁", reply_markup=time_of_deliveo)
    if message.text == "Пряный 🥬🥦":
        await message.answer("Выберите время для доставки 🎁", reply_markup=time_of_deliveo)
    if message.text == "Десертный 🍫🍦":
        await message.answer("Выберите время для доставки 🎁", reply_markup=time_of_deliveo)
    if message.text == "Авторский 🍔🌭":
        await message.answer("Выберите время для доставки 🎁", reply_markup=time_of_deliveo)
    if message.text == "Привезти в течение 60 минут 6️⃣0️⃣":
        await message.answer("Данные для доставки 📜", reply_markup=Delivery)
    if message.text == "Привезти в течение 120 минут 1️⃣2️⃣0️⃣":
        await message.answer("Данные для доставки 📜", reply_markup=Delivery)
    if message.text == "Привезти в течение 180 минут 1️⃣8️⃣0️⃣":
        await message.answer("Данные для доставки 📜", reply_markup=Delivery)

# заказ принят
# @dp.message_handler()
# async def proccess_order_command(message: types.Message):
#     if message.text == None:
#         message_text = text(
#             ("Спасибо. Ваш заказ принят."),
#             )   
#     await message.answer(message_text, parse_mode=ParseMode.MARKDOWN)

#повтор действий
@dp.message_handler()
async def echo_messege(message: types.Message):
    message_text = text(
        ("Необходимо выбрать нужное действие."),
        italic("\nНапоминаю, какие есть виды действий:"),
        code("/help")
        )   
    await message.reply(message_text, parse_mode=ParseMode.MARKDOWN)  


if __name__ == "__main__":
    executor.start_polling(dp) 