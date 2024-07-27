import discord
from discord.ext import commands
import random
import json

# FIRST GAME (cywe)
try:
    with open('../config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Ошибка: {e}")
    exit(1)

token_ds = config["token_ds"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="$")

@bot.command(name="flip")
async def flip(ctx):
    outcome = random.choice(["Heads", "Tails"])
    await ctx.send(f"{outcome}")