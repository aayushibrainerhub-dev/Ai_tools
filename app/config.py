from dotenv import load_dotenv
import os

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
GROK_API_CLOUD_KEY = os.getenv("GROK_API_CLOUD_KEY")