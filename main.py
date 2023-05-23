from API_request import get_price
import telebot

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'CMC api-key',
}


bot = telebot.TeleBot("telegram API-key")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Write /bitcoin to get a current bitcoin exchange rate(Provided by CoinMarketCap)")


@bot.message_handler(commands=['bitcoin'])
def send_xr(message):
    response = get_price(url, parameters, headers)
    bot.reply_to(message, '1 BTC = ' + str(round(float(response))) + ' USD')


bot.polling()
