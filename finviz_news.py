import finviz

class FinvizNews:
    news = []

    def __init__(self):
        news = self.news

    def get_news(self, ticker):
        self.news = finviz.get_news(ticker)

