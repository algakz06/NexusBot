import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import kbs

API_TOKEN = '5562182136:AAEmAr7SDM-lhPCdnzEOnmq6x1W45BXNysw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



async def about_sites(message: types.Message):
    await message.reply()
async def about_us(message: types.Message):
    await message.reply('''Нас выбирают по несклольким причинам:
\nМы не пытаемся продать свои услуги и пропасть. Мы строим долгосрочные отношения к каждым клиентом;
\nМы не навязываемся, и взаимодейсвуем с вами так, как вас удобно.
\nМы с вами заключим договор и сформируем ТЗ. Так вы точно будете уверены, что сайт будет таким, каким вы хотите.
''', )
async def link():
    pass


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Привет!\nНа связи команда Nexus Automation.\nМы поможем с выбором сайта и создадим его для вас.", reply_markup=kbs.main)


@dp.message_handler()
async def nav(message: types.Message):
    text = message.text
    if text == "Почему выбирают именно вас?":
        await message.answer('''Нас выбирают по несклольким причинам:
            \nМы не пытаемся продать свои услуги и пропасть. Мы строим долгосрочные отношения к каждым клиентом;
            \nМы не навязываемся, и взаимодейсвуем с вами так, как вас удобно.
            \nМы с вами заключим договор и сформируем ТЗ. Так вы точно будете уверены, что сайт будет таким, каким вы хотите.
            ''', reply_markup=kbs.aboutUs)
    elif text == "Я не разбираюсь в сайтах":
        pass
    elif text == "Связать со специалистом":
        await message.answer("Мы свяжемся с вами, как вам будет удобно", reply_markup=kbs.linkUs)
    elif text == "Главное меню":
        await message.answer('Вы вернулись в главное меню', reply_markup=kbs.main)
    elif text == "Свяжитесь со мной":
        await message.answer("Напишите, как и когда можно с вами связаться\nНапример: 89996086940, позвонить в Telegram, с 15:00 до 18:00", reply_markup=kbs.link_byMyself)
    elif text == "Свяжусь сам":
        await message.answer('''С нами можно связаться разными способами:
        Телефон 89996086940
        Telegram: https://t.me/Aleksandr_Zavorotnyy
        VK: https://vk.com/azavorotnyy
        WhatsApp: ''', reply_markup=kbs.links)
    elif text == "Сколько стоят ваши услуги?":
        await message.answer("lorem", reply_markup=kbs.services)
    elif text == "Почему цены такие низкие?":
        await message.answer('''Наши цены только кажутся низкими,
        потому что вы оцениваете нас на фоне остальных.
        Но если абстрогироваться ото всех остальных,
        то с уверенностью говорю вам, что наши цены являются достойными!
        \n\nКого бы вы не выбрали, задавайте вопросы и уточняйте моменты, волнующие вас''',
        reply_markup=ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton("Почему выбирают именно вас?")],
            [KeyboardButton("Главное меню")]
        ], resize_keyboard=True))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

