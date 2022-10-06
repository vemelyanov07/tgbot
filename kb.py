from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.emoji import emojize


#кнопки выбора кальяна
button1 = KeyboardButton("Стандарт")
button2 = KeyboardButton("Премиум")
button3 = KeyboardButton("Премиум +")
Standart_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, 
                                        one_time_keyboard=True).add(
                                        button1, button2, button3,
                                        )

#Кнопки вкуса кальянов
button4 = KeyboardButton("Свежий")
button5 = KeyboardButton("Кислый")
button6 = KeyboardButton("Сладкий")
button7 = KeyboardButton("Пряный")
button8 = KeyboardButton("Десертный")
button9 = KeyboardButton("Авторский")
taste_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                        one_time_keyboard=True).add(button4, button5, 
                                        button6, button7, button8, button9)

#кнопка доставки
button10 = KeyboardButton("Данные для доставки.")
Delivery = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Ваш номер для связи?", request_contact=True)
).add(
    KeyboardButton("Где Вы находитесь?", request_location=True)
)


#кнопки времени доставки
button11 = KeyboardButton("Выберите время доставки.")
time_of_deliveo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton("Привезти в течение 60 минут.")
).add(
    KeyboardButton("Привезти в течение 120 минут.")
).add(
    KeyboardButton("Привезти в течение 180 минут.")
)

#кнопки внутри бота
inline_button1 = InlineKeyboardButton("Стандарт", callback_data='button1')
inline_button2 = InlineKeyboardButton("Премиум", callback_data='button2')
inline_button3 = InlineKeyboardButton("Премиум +", callback_data='button3')

inline_keyboard1 = InlineKeyboardMarkup().add(inline_button1, 
                                        inline_button2, inline_button3)

inline_button4 = InlineKeyboardButton("Свежий", callback_data='button4')
inline_button5 = InlineKeyboardButton("Кислый", callback_data='button5')
inline_button6 = InlineKeyboardButton("Сладкий", callback_data='button6')
inline_button7 = InlineKeyboardButton("Пряный", callback_data='button7')
inline_button8 = InlineKeyboardButton("Десертный", callback_data='button8')
inline_button9 = InlineKeyboardButton("Авторский", callback_data='button9')

inline_keyboard2 = InlineKeyboardMarkup().add(inline_button4, 
                                        inline_button5, inline_button6, inline_button7, 
                                        inline_button8, inline_button9)


inline_button10 = InlineKeyboardButton("Ваш номер для связи?", request_location=True, callback_data='button11')
inline_button11 = InlineKeyboardButton("Где Вы находитесь?", request_location=True, callback_data='button12')

inline_keyboard3 = InlineKeyboardMarkup().add(inline_button10,
                                            inline_button11)


inline_button12 = InlineKeyboardButton("Привезти в течение 60 минут.", callback_data='button12')
inline_button13 = InlineKeyboardButton("Привезти в течение 120 минут.", callback_data='button13')
inline_button14 = InlineKeyboardButton("Привезти в течение 180 минут.", callback_data='button14')

inline_keyboard4 = InlineKeyboardMarkup().add(inline_button12).add(inline_button13).add(inline_button14)


