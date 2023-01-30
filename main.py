import discord
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
import os
from requests import get
import openai
import json
import asyncio
import youtube_dl
from discord.voice_client import VoiceClient
from pydub import AudioSegment
load_dotenv()
discordtoken = os.getenv("TOKEN")
openai_api_key = os.getenv("API_KEY")
openai.api_key = openai_api_key 


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}


@bot.event
async def on_ready():
    print("bot is ready")

#@bot.event
#async def on_message(message):
#    await message.content.lower()

@bot.command()
async def chat(ctx, *, message: str):
    response = openai.Completion.create(engine="text-davinci-002", prompt=message)
    await ctx.send(ctx.message.author.name ,response.choices[0].text)
    return

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
        voice_cal = await ctx.author.voice.channel.connect()
        info = ytdl.extract_info(url, download=False)
        audio_url = info["url"]
        voice_cal.play(discord.FFmpegPCMAudio(audio_url))
        #sound = AudioSegment.from_file(audio_url, format="mp3")
        #voice_cal.play(discord.FFmpegPCMAudio(sound))
    except discord.errors.ClientException:
        voice_client = ctx.voice_client
        await voice_client.disconnect()
@bot.command()
async def pause(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client and voice_client.is_playing():
        voice_client.pause()
        await ctx.send("Paused the current song.")
    else:
        await ctx.send("Not playing any song.")
@bot.command()
async def resume(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client:
        voice_client.resume()
        await ctx.send("resume the current song.")
    else:
        await ctx.send("Not playing any song.")

@bot.command()
async def stop(ctx):
       try:
            voice_client = ctx.voice_client
            await voice_client.disconnect()
       except:
            await ctx.send("not in a voice channel dont fool me")
bot.run(discordtoken)
