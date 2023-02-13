import discord
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
import os
from requests import get
import openai
import json
import asyncio
import requests
import time
import youtube_dl
from discord.voice_client import VoiceClient
from pydub import AudioSegment
from googletrans import Translator
from langdetect import detect
load_dotenv()
discordtoken = os.getenv("TOKEN")
openai_api_key = os.getenv("API_KEY")
openai.api_key = openai_api_key
news_key = os.getenv("NEWS_API_KEY")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}


@bot.event
async def on_ready():
    print("bot is ready")


@bot.command()
async def doc(ctx):
    embed = discord.Embed(title="List of available commands:", color=discord.Color.blue())
    embed.add_field(name="$chat", value="This command lets you have a conversation with the bot. Usage: $chat [message]")
    embed.add_field(name="$meme", value="This command sends a random meme. Usage: $meme")
    embed.add_field(name="$play", value="This command plays a YouTube video in the voice channel you are in. Usage: $play [YouTube video URL]")
    embed.add_field(name="$pause", value="This command pauses the currently playing YouTube video. Usage: $pause")
    embed.add_field(name="$resume", value="This command resumes the currently paused YouTube video. Usage: $resume")
    embed.add_field(name="$stop", value="This command stops the currently playing YouTube video. Usage: $stop")
    embed.add_field(name="$rdog", value="This command sends a random dog image. Usage: $rdog")
    embed.add_field(name="$translate", value="This command translates text to a specified language. Usage: $translate [language code] [text]")
    await ctx.send(embed=embed)


@bot.command()
async def chat(ctx, *, message: str = None):
    if message is None:
        await ctx.send(f"please enter somthing after **$chat** {ctx.message.author.mention}.")
        return
    try:        
        response = openai.Completion.create(engine="text-davinci-002", prompt=message)
        await ctx.send(f"{response.choices[0].text} ~{ctx.message.author.mention}")
        return
    except:
        await ctx.send(f"**AuthenticationError** Incorrect API key provided You can find your API key at https://platform.openai.com/account/api-keys. And please make your that you have internet connection")
        

@bot.command()
async def meme(ctx):
    content = get("https://meme-api.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.send(embed=meme)
    return

@bot.command()
async def play(ctx, url: str):
    try:
        voice_client = await ctx.author.voice.channel.connect()
        info = ytdl.extract_info(url, download=False)
        audio_url = info["url"]
        voice_client.play(discord.FFmpegPCMAudio(audio_url))
        #sound = AudioSegment.from_file(audio_url, format="mp3")
        #voice_client.play(discord.FFmpegPCMAudio(sound))
        if voice_client is None:
            voice_client = ctx.voice_client
            await voice_client.disconnect()
        
    except discord.errors.ClientException:
        await voice_client.disconnect()
    except AttributeError:
        await ctx.send(f"johin a voice channel")

@bot.command()
async def pause(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client and voice_client.is_playing():
        voice_client.pause()
        await ctx.send(f"Paused the current song {ctx.message.author.mention}.")
    else:
        await ctx.send(f"Not playing any song {ctx.message.author.mention}.")
@bot.command()
async def resume(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client:
        voice_client.resume()
        await ctx.send(f"resume the current song {ctx.message.author.mention}.")
    else:
        await ctx.send("fNot playing any song {ctx.message.author.mention}.")

@bot.command()
async def stop(ctx):
       try:
            voice_client = ctx.voice_client
            await voice_client.disconnect()
       except:
            await ctx.send(f"not in a voice channel dont fool me {ctx.message.author.mention}.")

@bot.command()
async def rdog(ctx):
    const = requests.get("https://random.dog/woof.json")
    stuff = json.loads(const.text)
    embed = discord.Embed(title=f"URL: {stuff['url']}", color = discord.Color.random())
    embed.set_image(url=f"{stuff['url']}")
    await ctx.send(embed=embed)

@bot.command()
async def translate(ctx, *, thing):
    translator = Translator()
    translation = translator.translate(thing).text
    await ctx.send(translation)

@bot.command()
async def news(ctx, innews):
    news = requests.get(f"https://newsapi.org/v2/everything?q={innews}&apiKey={news_key}").json()
    thnews = news["articles"]
    if news["status"] == "ok":
        for i , article in enumerate(thnews):
            if i < 5:
                emend = discord.Embed(title=article["title"], description=article["description"], url=article["url"],color=discord.Color.blue())
                await ctx.send(embed=emend)
            else:
                break
    else:
        await ctx.send(f"{innews} not found please try again")

bot.run(discordtoken)
