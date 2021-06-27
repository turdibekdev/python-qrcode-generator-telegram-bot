import telebot
from telebot import types
import pyqrcode

token = "1808028587:AAHFSP88B7cBOq_yWwpN7qZpzRvuQ"
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
	tugma = types.ReplyKeyboardMarkup(resize_keyboard=True)
	tugma1 = types.KeyboardButton("QR kod yaratish")
	tugma.add(tugma1)
	matn = "<b>Assalomu alaykum hurmatli foydalanuvchi, meni @turdibekdev va @pythonpractic kanallari sizga hizmat qilishim uchun yaratishdi. Men sizga QR kod yaratib beraman.</b>"
	bot.send_message(message.chat.id, matn, parse_mode="HTML", reply_markup=tugma)

@bot.message_handler(func=lambda message: True)
def tugma(message):
	if message.text == "QR kod yaratish":
		sent = bot.send_message(message.chat.id, "Menga url yoki matn jonating")
		bot.register_next_step_handler(sent, qrcode)
	else:
		bot.send_message(message.chat.id, "<b>Notog'ri buyruq</b>", parse_mode = "HTML", reply_markup = tugma)
		
def qrcode(qr):
	url = pyqrcode.create(qr.text)
	url.png("qrcode.png", scale = 15)
	bot.send_chat_action(qr.chat.id, "upload_document")
	bot.send_document(qr.chat.id, open("qrcode.png", "rb"))
	
bot.polling()