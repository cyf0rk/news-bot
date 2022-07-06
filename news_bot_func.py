import discord
import finviz_news
import api_client

from datetime import datetime

api_client = api_client.ApiClient()
news_api = finviz_news.FinvizNews()
client = discord.Client()
news_amount = 3;

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$') and len(message.content) <= 6 and message.content.isupper():
        message_content = message.content.replace('$', '')
        news_api.get_news(message_content)
        news = news_api.news

        for item in news[0:news_amount]:
            date = item[0]
            first_news_title = item[1]
            first_news_url = item[2]

            await message.channel.send(f'{date}\n{first_news_title}\n{first_news_url}')

client.run(api_client.discord_key)
