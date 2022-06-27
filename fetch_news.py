import requests
import api_client

api_client = api_client.ApiClient()

class NewsApi:
    news = []
    news_api_url = api_client.api_url
    news_api_key = api_client.api_key

    def __init__(self):
        self.news = []

    def getNews(self, ticker):
        self.news = self.fetchNews(ticker)
        return self.news

    def fetchNews(self, ticker):
        news_full_url = f'{self.news_api_url}&tickers={ticker}&apikey={self.news_api_key}'
        req = requests.get(news_full_url)
        data = req.json()
        data = data['feed']
        return data
