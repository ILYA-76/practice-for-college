from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup


class Keyboard:
    def keyBoardMain(self):
        keyboard = [

            [
                InlineKeyboardButton("Погода", callback_data="weather"),

            ],

        ]
        return InlineKeyboardMarkup(keyboard)

    def keyBoardToMain(self):
        keyboard = [
            [
                InlineKeyboardButton("Назад", callback_data="backToMain"),
            ],

        ]
        return InlineKeyboardMarkup(keyboard)

    def keyBoardDaily(self):
        keyboard = [

            [
                InlineKeyboardButton("Сегодня", callback_data="now"),
                InlineKeyboardButton("На завтра", callback_data="tomorrow"),
                InlineKeyboardButton("На неделю", callback_data="week"),
            ],
            [
                InlineKeyboardButton("Назад", callback_data="backToMain"),

            ],

        ]
        return InlineKeyboardMarkup(keyboard)





