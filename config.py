import os
from dotenv import load_dotenv

load_dotenv()

open_weather_token = os.getenv("OPEN_WEATHER_KEY")
tg_bot_token = os.getenv("TGBOT_KEY")