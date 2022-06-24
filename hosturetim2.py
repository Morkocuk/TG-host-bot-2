import telebot 
from telebot import types
import requests
bot = telebot.TeleBot(input('Enter Token : '))
@bot.message_handler(commands=['start'])
def start_msg(message):
    maac = types.InlineKeyboardMarkup()
    vodka = types.InlineKeyboardButton(text='Coder',url='https://t.me/Morkolive')
    make = types.InlineKeyboardButton(text="Host Oluştur",callback_data='make')
    maac.row_width = 2
    maac.add(make)
    bot.send_message(chat_id=message.chat.id,text=f'*Hi {message.from_user.first_name}\n- - - - - - - - - - - - -\nHoşgeldin  Botumuz İle Bedava Bir Şekilde Host Oluşturabilirsin!\n- - - - - - - - - - - - -\n 📌Yapımcı : @Morkolive*',parse_mode='markdown',reply_to_message_id=message.message_id,reply_markup=maac)
@bot.callback_query_handler(func=lambda message:True)
def call(message):
    if message.data == 'make':
        host = requests.get('https://apisx.pythonanywhere.com/Host/Maker').json()['result']
        user = host['user']
        email = host['email']
        passw = host['pass']
        login = host['login']
        web_url = host['Website-Url']
        log = f"<a href='{login}'>Tıkla</a>"  
        name = f"<a href='{message.from_user.first_name}'>{message.from_user.first_name}</a>" 
        maac = types.InlineKeyboardMarkup()
        make = types.InlineKeyboardButton(text="Host Oluştur",callback_data='make2')
        maac.row_width = 2
        maac.add(make)
        bot.edit_message_text(chat_id=(message.message.chat.id),message_id=(message.message.id),text=f'<b> {name}\n- - - - - - - -\n📩E-Posta : {email}\n👤Kullanıcı Adı : {user}\n🔑Şifre : {passw}\n🖇️Giriş Link : {log}\n☣️Website Link : {web_url}\n- - - - - - - -\n📌Yapımcı : @Morkolive</b>',parse_mode='html',reply_markup=maac,disable_web_page_preview=True)
    if message.data == 'make2':
        host2 = requests.get('https://apisx.pythonanywhere.com/Host/Maker').json()['result']
        user = host2['user']
        email = host2['email']
        passw = host2['pass']
        login = host2['login']
        web_url = host2['Website-Url']
        log = f"<a href='{login}'>Login-Url</a>"  
        name = f"<a href='{message.from_user.first_name}'>{message.from_user.first_name}</a>" 
        maac = types.InlineKeyboardMarkup()
        make = types.InlineKeyboardButton(text="Host Oluştur",callback_data='make2')
        maac.row_width = 2
        maac.add(make)
        bot.edit_message_text(chat_id=(message.message.chat.id),message_id=(message.message.id),text=f'<b>Merhaba {name}\n- - - - - - - -\n📩E-Posta : {email}\n👤Kullanıcı Adı : {user}\n🔑Şifre : {passw}\n🖇️Giriş Link  : {log}\n☣️Website Link : {web_url}\n- - - - - - - -\n📌Yapımcı : @Morkolive</b>',parse_mode='html',reply_markup=maac,disable_web_page_preview=True)
bot.polling(True)