import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import openai
api_keys = ".env_openai"
openai.api_key_path = api_keys


load_dotenv()
mytoken = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def chat(ctx, *, message: str):
    response = openai.Completion.create(engine="text-davinci-002", prompt=message)
    await ctx.send(response.choices[0].text)
    return


bot.run(mytoken)
