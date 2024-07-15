import discord
from discord.ext import commands
import random
import json

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

    if "слава украине" in message.content.lower():
        await message.reply("в составе РОССИИ!!!")

    if "иди нахуй" in message.content.lower():
        await message.reply("Своим помахуй")

bot.run(token_ds)
