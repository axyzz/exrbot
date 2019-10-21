import requests
import telebot
bot = telebot.TeleBot("705393130:AAHkmkZ0D9AhoR9iH8Dl8eu7ZeVTsuPzuew")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Write /bitcoin to get a current bitcoin exchange rate(Provided by CoinMarketCap)")


@bot.message_handler(commands=['bitcoin'])
def send_xr(message):
    bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    bot.reply_to(message, '1 BTC = ' + str(round(float(response_json[0]['price_usd']))) + ' USD')


bot.polling()
