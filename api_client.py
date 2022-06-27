import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class ApiClient:
    def __init__(self):
        self.discord_key = os.getenv('DISCORD_KEY')
        self.api_url = os.getenv('API_URL')
        self.api_key = os.getenv('API_KEY')
