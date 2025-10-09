import asyncio
import logging
import wikipedia
from deep_translator import GoogleTranslator
from rmkp import reply_keyboard as rb
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

Token = "8236110827:AAEkqbY9dQvKDkHS6LV3qAJwcciEgeBTsZA"

user_lang = {}
logging.basicConfig(level=logging.INFO)

bot = Bot(token=Token)
dp = Dispatcher()

translations = {
    "uz": "Siz o‘zbek tilini tanladingiz ✅",
    "ar": "لقد اخترت اللغة العربية  ✅",
    "kk": "Сіз қазақ тілін таңдадыңыз  ✅",
    "ky": "Сиз кыргыз тилин тандадыңыз  ✅",
    "tg": "Шумо забони тоҷикро интихоб кардед  ✅",
    "tk": "Siz türkmen dilini saýladyňyz  ✅",
    "en": "You have selected English  ✅",
    "ru": "Вы выбрали русский язык  ✅"
}

send = {
    "uz": "Sorov yuboring.",
    "ar": "أرسل طلبًا",
    "kk": "Сұраныс жіберіңіз.",
    "ky": "Сурам жөнөтүңүз.",
    "tg": "Дархост фиристед.",
    "tk": "Sorag iberiň.",
    "en": "Send a request.",
    "ru": "Отправьте запрос."
}

lang_names = {
    "uz": "Uzbek",
    "ar": "Arabic",
    "kk": "Kazakh",
    "ky": "Kyrgyz",
    "tg": "Tajik",
    "tk": "Turkmen",
    "en": "English",
    "ru": "Russian"
}

@dp.message(Command("start"))
async def welcome(message: Message):
    await message.answer("Welcome to WikiBot!")
    await message.answer("Please choose one language from the menu ⬇️", reply_markup=rb())

@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Send a request and I will send you information according to your request. "
                        "Also you may change your language to other language with /changemyleng command."
                        )

@dp.message(Command("changemylang"))
async def changelang(message: Message):
    lang = user_lang.get(message.from_user.id, "uz")
    name = lang_names.get(lang, lang)
    await message.answer(f"Your language is {name} now. Choose other language ⬇️", reply_markup=rb())

@dp.message()
async def reply_test(message: Message):
    if message.text == "🇺🇿 O‘zbekcha":
        user_lang[message.from_user.id] = "uz"
        wikipedia.set_lang("uz")
        await message.answer(translations["uz"], reply_markup=ReplyKeyboardRemove())
        await message.answer(send["uz"])
    elif message.text == "🇸🇦 العربية":
        user_lang[message.from_user.id] = "ar"
        wikipedia.set_lang("ar")
        await message.answer(translations["ar"], reply_markup=ReplyKeyboardRemove())
        await message.answer(send["ar"])
    elif message.text == "🇰🇿 Қазақша":
        user_lang[message.from_user.id] = "kk"
        wikipedia.set_lang("kk")
        await message.answer(translations["kk"], reply_markup=ReplyKeyboardRemove())
        await message.answer(send["kk"])
    elif message.text == "🇰🇬 Кыргызча":
        user_lang[message.from_user.id] = "ky"
        wikipedia.set_lang("ky")
        await message.answer(translations["ky"], reply_markup=ReplyKeyboardRemove())
        await message.answer(send["ky"])
    elif message.text == "🇹🇯 Тоҷикӣ":
        user_lang[message.from_user.id] = "tg"
        wikipedia.set_lang("tg")
        await message.answer(translations["tg"], reply_markup=ReplyKeyboardRemove())
        await message.answer(send["tg"])
    elif message.text == "🇹🇲 Türkmençe":
        user_lang[message.from_user.id] = "tk"
        wikipedia.set_lang("tk")
        await message.answer(translations["tk"], reply_markup=ReplyKeyboardRemove())
        await message.answer(send["tk"])
    elif message.text == "🇬🇧 English":
        user_lang[message.from_user.id] = "en"
        wikipedia.set_lang("en")
        await message.answer(translations["en"], reply_markup=ReplyKeyboardRemove())
        await message.answer(send["en"])
    elif message.text == "🇷🇺 Russian":
        user_lang[message.from_user.id] = "ru"
        wikipedia.set_lang("ru")
        await message.answer(translations["ru"], reply_markup=ReplyKeyboardRemove())
        await message.answer(send["ru"])

    if message.from_user.id not in user_lang:
        await message.answer("Please choose one language from the menu ⬇️", reply_markup=rb())
        return

    try:
        response = message.text
        lang = user_lang.get(message.from_user.id, "uz")
        wikipedia.set_lang(lang)
        result = wikipedia.summary(response, sentences=7)
        await message.answer(result)
    except:
        lang = user_lang.get(message.from_user.id, "uz")
        text = "Kechirasiz. Bu mavzu bo'yicha ma'lumot topa topilmadi"
        translated = GoogleTranslator(source="uz", target=lang).translate(text)
        await message.reply(translated)

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
