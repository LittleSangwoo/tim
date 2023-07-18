import telebot
import datetime
import time

# Replace YOUR_TOKEN with your own Telegram bot token
bot = telebot.TeleBot('6054611943:AAEyntxtnXX2acTLS4bpXm2duHWCRBl6oL4')

# Replace CHAT_ID with your own chat ID
chat_id = '1088963029'

#942022819
def send_hello():
    # Replace "Привет" with your own message
    bot.send_message(chat_id, "Доброе утро, мой котёнок💗✨")
    


def send_huy():
    # Replace "Привет" with your own message
    bot.send_message(chat_id, "Сладких снов, мой милый мальчик💗✨")
    bot.send_message(chat_id, "Спи сладко")


def send_ly():
    # Replace "Привет" with your own message
    bot.send_message(chat_id, "я люблю тебя")




while True:
        now = datetime.datetime.now()
        if now.hour == 0 and now.minute == 56:
            send_hello()
            time.sleep(60)   # Подождать минуту, чтобы не отправлять сообщение несколько раз

        elif now.hour == 0 and now.minute == 57:
            send_ly()
            time.sleep(60)

        elif now.hour == 0 and now.minute == 58:
            send_huy()
            time.sleep(60)


        elif now.hour == 0 and now.minute == 59:
            send_ly()
            time.sleep(60)
        
        else:
            time.sleep(30)  # Подождать 10 секунд и проверить время снова

        



bot.polling(non_stop=True, interval=0)