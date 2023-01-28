import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from requests import get
import openai
import json
load_dotenv()
discordtoken = os.getenv("TOKEN")
openai_api_key = os.getenv("API_KEY")
openai.api_key = openai_api_key 


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def chat(ctx, *, message: str):
    response = openai.Completion.create(engine="text-davinci-002", prompt=message)
    await ctx.send(response.choices[0].text)
    return

@bot.command()
async def meme(ctx):
    content = get("https://meme-api.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.send(embed=meme)
    return

bot.run(discordtoken)
