from telegram_bottools import telegram_bottools as bot

bot_config = (-11111111, 'xxxxxx:yyyyyyyyyyy')
message = 'Hello World!'

bot.send_message(*bot_config, message)