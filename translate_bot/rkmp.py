from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

def rb(): # see reply
    menu = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text="🇺🇿 O‘zbekcha"),
                KeyboardButton(text="🇸🇦 العربية")
            ],
            [
                KeyboardButton(text="🇰🇿 Қазақша"),
                KeyboardButton(text="🇰🇬 Кыргызча")
            ],
            [
                KeyboardButton(text="🇹🇯 Тоҷикӣ"),
                KeyboardButton(text="🇹🇲 Türkmençe")
            ],
            [
                KeyboardButton(text="🇬🇧 English"),
                KeyboardButton(text="🇷🇺 Русский") 
            ],
            [
                KeyboardButton(text="🇫🇷 Français"),
                KeyboardButton(text="🇩🇪 Deutsch")
            ],
            [
                KeyboardButton(text="🇮🇹 Italiano"),
                KeyboardButton(text="🇪🇸 Español")
            ],
            [
                KeyboardButton(text="🇵🇹 Português"),
                KeyboardButton(text="🇹🇷 Türkçe")
            ],
            [
                KeyboardButton(text="🇨🇳 中文"),
                KeyboardButton(text="🇯🇵 日本語")
            ],
            [
                KeyboardButton(text="🇮🇳 हिन्दी"),
                KeyboardButton(text="🇰🇷 한국어")
            ],
            [
                KeyboardButton(text="🇵🇰 اردو"),
                KeyboardButton(text="🇮🇷 فارسی")
            ]
        ],
        resize_button = True
    )
    return menu