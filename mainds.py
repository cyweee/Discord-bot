import discord
from discord.ext import commands
import random
import json
import os
import yt_dlp as youtube_dl
import asyncio

try:
    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Ошибка при загрузке конфигурации: {e}")
    exit(1)

token_ds = config["token_ds"]
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix="$")

# cywe func begin

# configuration for yt-dlp
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

async def from_url(url, *, loop=None, stream=False):
    loop = loop or asyncio.get_event_loop()
    data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

    if 'entries' in data:
        data = data['entries'][0]

    filename = data['url'] if stream else ytdl.prepare_filename(data)
    return filename

@bot.command(name='join')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("you're not currently in a voice channel")
        return

    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='l')
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()

@bot.command(name='p')
async def play(ctx, url):
    async with ctx.typing():
        filename = await from_url(url, stream=True)
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=filename, **ffmpeg_options))
    await ctx.send(f'Now playing: {url}')

@bot.command(name='s')
async def stop(ctx):
    ctx.voice_client.stop()
# cywe func begin

# korvander's func begin
@bot.command()
async def random_word(ctx):
    random_response = random.choice(config["responses"])
    await ctx.send(random_response)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    if bot.user.mentioned_in(message):
        random_response = random.choice(config["responses"])
        await message.reply(random_response)

    elif "слава украине" in message.content.lower():
        await message.reply("в составе РОССИИ!!!")

    elif "иди нахуй" in message.content.lower():
        await message.reply("Своим помахуй")
    else:
        pass
# korvander's func finish


bot.run(token_ds)
