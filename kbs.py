from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=
    [
        [KeyboardButton("Я не разбираюсь в сайтах")],
        [KeyboardButton("Почему выбирают именно вас?")],
        [KeyboardButton("Связать со специалистом")],
    ], resize_keyboard=True)

aboutUs = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton("Сколько стоят ваши услуги?"),
        KeyboardButton("Связать со специалистом")
    ],
    [
        KeyboardButton("Главное меню"),
    ],
], resize_keyboard=True)

linkUs = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton("Свяжусь сам"),
        KeyboardButton("Свяжитесь со мной")
    ],
    [
        KeyboardButton("Главное меню"),
    ],
], resize_keyboard=True)

link_byMyself = ReplyKeyboardMarkup(keyboard=[      #client will link us by himself
    [
        KeyboardButton("Свяжусь сам"),
    ],
    [
        KeyboardButton("Главное меню"),
    ],
], resize_keyboard=True)

#Our messangers for connection
links = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton("Позвонить")
    ],
    [
        KeyboardButton("VK"),
        KeyboardButton("Telegram"),
        KeyboardButton("What's app"),
    ],
    [
        KeyboardButton("Свяжитесь со мной")
    ],
    [
        KeyboardButton("Главное меню"),
    ],
], resize_keyboard=True)

services = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton("Почему цены такие низкие?"),
        KeyboardButton("Связать со специалистом")
    ],
    [
        KeyboardButton("Главное меню"),
    ],
], resize_keyboard=True)