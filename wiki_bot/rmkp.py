from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def reply_keyboard():
    menu = ReplyKeyboardMarkup(
        keyboard=[
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
                KeyboardButton(text="🇷🇺 Russian") 
            ]
        ],
        resize_keyboard=True
    )
    return menu