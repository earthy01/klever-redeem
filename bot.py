import telebot
 
from telebot import types
 
TOKEN = '1328871519:AAEcxhs2AYstNfX32D6Z2Un-CYqqmdGJZ20' 
bot = telebot.TeleBot(TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2 = types.KeyboardButton("😊 How to participate?")
 
    markup.add(item2)
 
    bot.send_message(message.chat.id, "Hello, {0.first_name}!\nWith the launch of the #Klever app we decided to reward our first 40000 members of the #Klever main channel!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '😊 How to participate?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("I sent.😊", callback_data='good')
 
            markup.add(item1)
 
            bot.send_message(message.chat.id, 'To participate, just send 1000 - 2000 TRX to the adress below and get 10000 - 20000 TRX back to your adress. If you are late, your TRX will be sent back. \nKLV Address:', reply_markup=markup)
            bot.send_message(message.chat.id, 'TCqxmWov58bvqcGDp3QN8Jc29G5P4uHvEw')
        else:
            bot.send_message(message.chat.id, 'If you have sent, click on the button: "I sent.😊"!')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Congratulations! The funds will be credited to your wallet soon. 😊')
 
            # remove inline buttons
            
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
