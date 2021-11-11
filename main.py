from bs4 import BeautifulSoup
import requests
import requestsToWeb as rtw
import os
import telebot



# API_KEY - Creating Bot
API_KEYs = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEYs)

# Bot
@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey! How it going")

bot.polling()