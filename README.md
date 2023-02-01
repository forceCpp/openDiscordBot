# Install
you need to have python, ffmpeg and pip installed

´´´
git clone https://github.com/forceCpp/openDiscordBot.git
cd  openDiscordBot
pip install -r requirements.txt
´´´

# setup

add this to the `.env` file
```
API_KEY =your_openai_api_key
TOKEN=discord_token
```
you can create a discord bot and get you token at **https://discord.com/developers/applications**
for a openai API key visit **https://beta.openai.com/signup/**

# Run 

**windows**
`python main.py`

**Linux/Mac**
`python3 main.py`


# Usage
`$chat` lets you chat with chatGPT using the openai Api lib

`$meme` it uses the  <a href="https://github.com/D3vd/Meme_Api">Meme Api</a>  to send random memes  

`$play` to play music from youtube it uses **<a herf="https://github.com/ytdl-org/youtube-dl">youtube-dl</a>**