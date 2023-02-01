# Install
you need to have **<a href="https://www.python.org/">python</a>** and **<a href="https://ffmpeg.org/download.html">ffmpeg</a>** installed

```
git clone https://github.com/forceCpp/openDiscordBot.git
cd  openDiscordBot
pip install -r requirements.txt
```

# setup

add this to the `.env` file

```
API_KEY =your_openai_api_key
TOKEN=discord_token
```
you can create a discord bot and get you token at **https://discord.com/developers/applications**
for a openai API key visit **https://beta.openai.com/signup/**

# Run 

**Windows**
`python main.py`

**Linux/Mac**
`python3 main.py`


# Usage
`$chat` lets you chat with chatGPT using the openai Api lib

`$meme` it uses the  <a href="https://github.com/D3vd/Meme_Api">Meme Api</a>  to send random memes  

`$play` to play music from youtube it uses <a href="https://github.com/ytdl-org/youtube-dl">youtube-dl</a>

# try
give the bot a try 
> **note** its not allways online cuz i am stil working on it
but when its done it will be online for ever


` https://discord.com/api/oauth2/authorize?client_id=1068497688628305970&permissions=8&scope=bot `