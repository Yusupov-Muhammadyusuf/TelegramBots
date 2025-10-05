import asyncio
import logging
from rkmp import rb
from deep_translator import GoogleTranslator
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command

Token = "8308423032:AAG73U82HQ0LZ8grfylBgA3SW7aYJbuqEe0"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=Token)
dp = Dispatcher()

user_languages = {}

@dp.message(Command("start"))
async def welcome(message: Message):
    await message.answer("Hello, welcome to the Doppi Translator bot!")
    await message.answer("Please select your preferred language from the menu ⬇️", reply_markup=rb())

@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Select any language from the menu and send a message. The bot will translate your message into the language you selected.\nTo change the language use the /changemylang command!")

@dp.message(Command("mylang"))
async def seelang(message: Message):
    await message.answer(f"Currently your language is {lang}.")

@dp.message(Command("changemylang"))
async def newlang(message: Message):
    await message.answer(f"Currently your language is {lang}. Please select another language from the menu ⬇️", reply_markup=rb())

@dp.message()
async def translate(message: Message):
    if message.text == "🇺🇿 O‘zbekcha":
        user_languages[message.from_user.id] = "uz"
        await message.answer("You have selected Uzbek  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("Start!")
        return

    elif message.text == "🇸🇦 العربية":
        user_languages[message.from_user.id] = "ar"
        await message.answer("لقد اخترت اللغة العربية  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("ابدأ!")
        return

    elif message.text == "🇰🇿 Қазақша":
        user_languages[message.from_user.id] = "kk"
        await message.answer("Сіз қазақ тілін таңдадыңыз  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("Бастау!")
        return

    elif message.text == "🇰🇬 Кыргызча":
        user_languages[message.from_user.id] = "ky"
        await message.answer("Сиз кыргыз тилин тандадыңыз  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("Башта!")
        return

    elif message.text == "🇹🇯 Тоҷикӣ":
        user_languages[message.from_user.id] = "tg"
        await message.answer("Шумо забони тоҷикӣ интихоб кардед  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("Оғоз кунед!")
        return

    elif message.text == "🇹🇲 Türkmençe":
        user_languages[message.from_user.id] = "tk"
        await message.answer("Siz türkmen dilini saýladyňyz  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("Başlaň!")
        return

    elif message.text == "🇬🇧 English":
        user_languages[message.from_user.id] = "en"
        await message.answer("You have selected English  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("Start!")
        return

    elif message.text == "🇷🇺 Русский":
        user_languages[message.from_user.id] = "ru"
        await message.answer("Вы выбрали русский язык  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("Начать!")
        return

    elif message.text == "🇫🇷 Français":
        user_languages[message.from_user.id] = "fr"
        await message.answer("Vous avez choisi le français  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("Commencer!")
        return

    elif message.text == "🇩🇪 Deutsch":
        user_languages[message.from_user.id] = "de"
        await message.answer("Sie haben Deutsch gewählt  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("Starten!")
        return

    elif message.text == "🇮🇹 Italiano":
        user_languages[message.from_user.id] = "it"
        await message.answer("Hai selezionato l'italiano  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("Inizia!")
        return

    elif message.text == "🇪🇸 Español":
        user_languages[message.from_user.id] = "es"
        await message.answer("Has seleccionado español  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("¡Comenzar!")
        return

    elif message.text == "🇵🇹 Português":
        user_languages[message.from_user.id] = "pt"
        await message.answer("Você selecionou português  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("Começar!")
        return

    elif message.text == "🇹🇷 Türkçe":
        user_languages[message.from_user.id] = "tr"
        await message.answer("Türkçe’yi seçtiniz  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("Başla!")
        return

    elif message.text == "🇨🇳 中文":
        user_languages[message.from_user.id] = "zh-CN"
        await message.answer("您选择了中文  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("开始!")
        return

    elif message.text == "🇯🇵 日本語":
        user_languages[message.from_user.id] = "ja"
        await message.answer("日本語を選択しました  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("開始!")
        return

    elif message.text == "🇮🇳 हिन्दी":
        user_languages[message.from_user.id] = "hi"
        await message.answer("आपने हिन्दी चुनी है  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("शुरू करें!")
        return

    elif message.text == "🇰🇷 한국어":
        user_languages[message.from_user.id] = "ko"
        await message.answer("한국어를 선택하셨습니다  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("시작!")
        return

    elif message.text == "🇵🇰 اردو":
        user_languages[message.from_user.id] = "ur"
        await message.answer("آپ نے اردو منتخب کی  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("شروع کریں!")
        return

    elif message.text == "🇮🇷 فارسی":
        user_languages[message.from_user.id] = "fa"
        await message.answer("شما فارسی را انتخاب کردید  ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("شروع کنید!")
        return

    text = message.text
    user_lang = user_languages.get(message.from_user.id, "uz")
    translate_text = GoogleTranslator(source="auto", target=user_lang).translate(text)
    await message.answer(translate_text)

async def main():                                               
    await dp.start_polling(bot)                                           

if __name__=="__main__":
    asyncio.run(main())
