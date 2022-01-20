import time
from datetime import datetime

from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from Contents import Content
from Keyboard import Keyboard


class BrainOfBot:

    def __init__(self):
        self.dicOfState = {}
        self.missTake = 0

    def do_echo(self, update: Update, context: CallbackContext, ):
        userId = update.effective_user.id
        if self.dicOfState[userId] == "weather":
            text = update.message.text
            if Content().jsonOfAPI(text) != "ERROR_IN_JSON_API":
                self.data = Content().jsonOfAPI(text)

                update.message.reply_text(
                    f"Сегодня в вашем городе {self.data[0]['temp']['day']}℃\n"
                    "\n"
                    f"Днем {self.data[0]['temp']['day']}\n"
                    f"Ночью {self.data[0]['temp']['night']}℃\n"
                    f"Облачность {self.data[0]['clouds']}%\n"
                    f"Днем ощущаестя как {self.data[0]['feels_like']['day']}℃\n"
                    f"Ночью ощущаестя как {self.data[0]['feels_like']['night']}℃\n",
                    reply_markup=Keyboard().keyBoardDaily()
                )
            else:
                if self.missTake == 0:
                    update.message.reply_photo(
                        caption="ПОПРОБУЙ ЕЩЕ РАЗ",
                        reply_markup=Keyboard().keyBoardToMain(),
                    )




    def keyboardHendler(self, update: Update, bot: Bot, chat_data=None, **kwargs):
        query = update.callback_query
        data = query.data
        userId = update.effective_user.id
        if data == "weather":
            self.dicOfState[userId] = "weather"
            update.effective_message.reply_text(
                "Где узнаем погоду?",
                reply_markup=Keyboard().keyBoardToMain()
            )

        elif data == "now":
            query.edit_message_text(
                f"Сегодня в вашем городе {self.data[0]['temp']['day']}℃\n"
                "\n"
                f"Днем {self.data[0]['temp']['day']}\n"
                f"Ночью {self.data[0]['temp']['night']}℃\n"
                f"Облачность {self.data[0]['clouds']}%\n"
                f"Днем ощущаестя как {self.data[0]['feels_like']['day']}℃\n"
                f"Ночью ощущаестя как {self.data[0]['feels_like']['night']}℃\n",
                reply_markup=Keyboard().keyBoardDaily()
            )
        elif data == "tomorrow":
            query.edit_message_text(
                f"Завтра в вашем городе {self.data[1]['temp']['day']}℃\n"
                "\n"
                f"Днем {self.data[1]['temp']['day']}\n"
                f"Ночью {self.data[1]['temp']['night']}℃\n"
                f"Облачность {self.data[1]['clouds']}%\n"
                f"Днем ощущаестя как {self.data[1]['feels_like']['day']}℃\n"
                f"Ночью ощущаестя как {self.data[1]['feels_like']['night']}℃\n",
                reply_markup=Keyboard().keyBoardDaily()
            )
        elif data == "week":
            days = datetime.now()
            listOfDaysForWeather = []
            i = 0
            if days.month < 10:
                month = "0" + str(days.month)
            else:
                month = days.month
            for day in self.data:
                listOfDaysForWeather.append(day['temp']['day'])
                i += 1
            query.edit_message_text(
                f"Сегодня {listOfDaysForWeather[0]}℃\n"
                f"Завтра {listOfDaysForWeather[1]}℃\n"
                f"Послезавтра  {listOfDaysForWeather[2]}℃\n"
                f"{days.day + 3}.{month}  {listOfDaysForWeather[3]} ℃\n"
                f"{days.day + 4}.{month}  {listOfDaysForWeather[3]} ℃\n"
                f"{days.day + 5}.{month}  {listOfDaysForWeather[4]} ℃\n"
                f"{days.day + 6}.{month}  {listOfDaysForWeather[5]} ℃\n",
                reply_markup=Keyboard().keyBoardDaily(),
            )


    def main(self, ):
        print("Поехали")

        updater = Updater(
            token='5052499066:AAFtuqIs70e2Ie8osqT-J6yDlJJd-Stl3xI',
        )

        updater.dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=self.do_echo))
        updater.dispatcher.add_handler(CallbackQueryHandler(callback=self.keyboardHendler))
        updater.dispatcher.add_handler(MessageHandler(filters=Filters.sticker, callback=self.do_echo))

        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    BrainOfBot().main()