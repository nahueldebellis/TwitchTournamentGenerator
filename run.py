import sys
sys.path.append('src')
from bot import Bot

if __name__ ==  "__main__":
    try:
        bot = Bot()
        bot.run()
    except Exception as error:
        print(f'bot error: {error}')

