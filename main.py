from bs4 import BeautifulSoup
import requests
from telebot.types import Message
import requestsToWeb as rtw
import os
import telebot
import BotProperties as Bp
from dotenv import load_dotenv

load_dotenv()

Api_Key = os.getenv('API_KEY')

# API_KEY - Creating Bot
bot = telebot.TeleBot("2142199446:AAFOkcDk5sTu6-a05nkSYpeC5GmcaHNqklk")

# Bot basic commands
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hallo ;) \nSchick mir ein Wort.🙂 ")

@bot.message_handler(commands=['Über'])
def start(message):
    bot.reply_to(message, "Ich bin ein Bote, Ich hilfe dir mit die Artikel in Deutsch!\n ")

# Bots body
@bot.message_handler(func=Bp.TruePasser)
def  wordRequest(message):
    if Bp.wordRequestCheck(message.text):
        word = rtw.wordInstance(message.text)
        Artikel = word.Artikel
        meaning = word.Meaning()
        if Artikel =="der":
            colorbox = "🔵"
        elif Artikel =="die":
            colorbox = "🔴"
        elif Artikel =="das":
            colorbox = "🟢"
        else:
            colorbox = "🟡"

        if Artikel == "None":
            bot.reply_to(message,f"{colorbox} *{message.text}*\nkeinen Artikel Finden🤕")
        else:
            Composed = word.TableComposer(Artikel)
            Composed = Composed.replace(u"Ã¤",u"ä").replace(u"Ã¼",u"ü").replace(u"Ã",u"ß")
            bot.reply_to(message, f"{colorbox} {Artikel} {message.text} \n-------------\n {meaning} \n-------------\n \n{Composed}")


    
bot.polling()