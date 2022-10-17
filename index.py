import telebot
import requests
# Создаем экземпляр бота
bot = telebot.TeleBot('HERE TGBot API KEY')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет. В этом боте ты сможешь сгенерировать QR код. Просто отправь мне любое сообщение, а в ответ я пришлю тебе QR код.')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Сейчас сгенерирую код: ' + message.text)
    url = "https://secret.herokuapp.com/QR/" + message.text
    payload = ""
    response = requests.request("POST", url, data=payload)
# Запускаем бота
bot.polling(none_stop=True, interval=0)
