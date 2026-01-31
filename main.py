import telebot
import google.generativeai as genai
from flask import Flask
from threading import Thread

# زانیاریێن تە
BOT_TOKEN = "8387075466:AAFnBSzqxc18w3vFYeKyCQwKrOsbksyCq7Q"
GEMINI_KEY = "AIzaSyAhUBuEbCWAYvwM4553ow35vkkdfLoc6bU"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask('')
@app.route('/')
def home(): return "XaniAI is Live!"

def run_flask(): app.run(host='0.0.0.0', port=8080)

system_instruction = "تۆ XaniAI ی، تەنها بە زاراوەی بادینی وەڵام بدەوە."

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = model.generate_content(f"{system_instruction}\nبەکارهێنەر: {message.text}")
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "ببوورە برا، کێشەیەکا تەکنیکی هەیه. تۆزەکا دی تاقی بکە.")

if __name__ == "__main__":
    Thread(target=run_flask).start()
    bot.infinity_polling()
