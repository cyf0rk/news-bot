import discord
import fetch_news
import api_client

from datetime import datetime

api_client = api_client.ApiClient()
news_api = fetch_news.NewsApi()
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$') and len(message.content) <= 6 and message.content.isupper():
        message_content = message.content.replace('$', '')
        news = news_api.getNews(message_content)

        for item in news[0:3]:
            first_news_title = item['title']
            first_news_summary = item['summary']
            first_news_url = item['url']
            date = datetime.strptime(item['time_published'], '%Y%m%dT%H%M%S')

            await message.channel.send(f'{date}\n{first_news_title}\n\n{first_news_summary}\n{first_news_url}')

client.run(api_client.discord_key)
