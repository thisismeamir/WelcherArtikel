from bs4 import BeautifulSoup
import requests
import requestsToWeb as rtw
import os
import telebot



# API_KEY - Creating Bot
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

# Bot
@bot.message_handler(command=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey! How it going")

bot.polling()