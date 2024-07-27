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

class ShooterGame:
    def __init__(self):
        self.player_health = 105
        self.enemy_health = 100
        self.player_potions = 2
        self.enemy_potions = 1

    def attack(self):
        player_damage = random.randint(10, 30)
        enemy_damage = random.randint(5, 25)
        self.enemy_health -= player_damage
        self.player_health -= enemy_damage
        if self.player_health <= 0:
            return f"You have dealt {player_damage} damage. The enemy has inflicted {enemy_damage} damage. You lose."
        elif self.enemy_health <= 0:
            return f"You have dealt {player_damage} damage. The enemy has inflicted {enemy_damage} damage. You win"
        else:
            return f"You have dealt {player_damage} damage. The enemy has inflicted {enemy_damage} damage. Your health: {self.player_health}. Enemy Health: {self.enemy_health}."

    def use_potion(self):
        if self.player_potions > 0:
            heal_amount = random.randint(15, 30)
            self.player_health += heal_amount
            self.player_potions -= 1
            return f"You used the potion and restored {heal_amount} health. Your current health: {self.player_health}. Potions remaining: {self.player_potions}."
        else:
            return "You have no potions left!"

    def enemy_use_potion(self):
        if self.enemy_potions > 0:
            heal_amount = random.randint(15, 30)
            self.enemy_health += heal_amount
            self.enemy_potions -= 1
            return f"The enemy used the potion and restored the {heal_amount} Health. Enemy Health: {self.enemy_health}. The enemy has potions left: {self.enemy_potions}."
        else:
            return "The enemy has no potions!"

    def dodge(self):
        if random.random() < 0.5:
            return "You have dodged the enemy's attack!"
        else:
            enemy_damage = random.randint(5, 25)
            self.player_health -= enemy_damage
            if self.player_health <= 0:
                return f"You tried to dodge, but failed. The enemy struck {enemy_damage} damage. You've loses."
            else:
                return f"You tried to dodge, but failed. The enemy struck {enemy_damage} Damage. Your current health: {self.player_health}."


games = {}

@bot.command(name="start_shooter")
async def start_shooter(ctx):
    game = ShooterGame()
    games[ctx.author.id] = game
    await ctx.send("Game on! You have encountered an enemy. Use the commands $attack, $use_potion or $dodge.")

@bot.command(name="attack")
async def attack(ctx):
    if ctx.author.id not in games:
        await ctx.send("First, start the game using the $start_shooter command.")
        return
    game = games[ctx.author.id]
    result = game.attack()
    await ctx.send(result)
    if "lose" in result or "win" in result:
        del games[ctx.author.id]
        return

    # the enemy can bit you or take a potion
    if game.enemy_potions > 0 and random.random() < 0.3:
        enemy_result = game.enemy_use_potion()
    else:
        enemy_result = None

    if enemy_result:
        await ctx.send(enemy_result)
    else:
        enemy_damage = random.randint(5, 25)
        game.player_health -= enemy_damage
        await ctx.send(f"The enemy has attacked and inflicted upon you {enemy_damage} Damage. Your current health: {game.player_health}")

    if game.player_health <= 0:
        await ctx.send("You lose.")
        del games[ctx.author.id]
    elif game.enemy_health <= 0:
        await ctx.send("You win!")
        del games[ctx.author.id]

@bot.command(name="use_potion")
async def use_potion(ctx):
    if ctx.author.id not in games:
        await ctx.send("First, start the game using the $start_shooter command.")
        return
    game = games[ctx.author.id]
    result = game.use_potion()
    await ctx.send(result)

@bot.command(name="dodge")
async def dodge(ctx):
    if ctx.author.id not in games:
        await ctx.send("First, start the game using the $start_shooter command.")
        return
    game = games[ctx.author.id]
    result = game.dodge()
    await ctx.send(result)
    if "lose" in result:
        del games[ctx.author.id]

# SECOND GAME
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')