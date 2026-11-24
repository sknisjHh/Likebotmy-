import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8779440342:AAFiXuTp3ZfiJDr7JraET9L0PnbVDFfjaZM"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Emoji Bhejo", callback_data="send_emoji")
    markup.add(button)

    bot.send_message(
        message.chat.id,
        "Neeche wale button pe click karo:",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "send_emoji")
def handle_emoji_click(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "🔥")

print("Bot chal raha hai...")
bot.infinity_polling()
