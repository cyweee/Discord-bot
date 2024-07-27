import discord
from discord.ext import commands
import random
import json

# FIRST GAME (cywe)
try:
    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Ошибка: {e}")
    exit(1)

token_ds = config["token_ds"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="$")

# Определение сообщений на разных языках
messages = {
    "ru": {
        "start": "Ты идешь по улице, и видишь развилку. Что будешь делать?\n1. Пойти по тропинке\n2. Развернуться и вернуться домой",
        "stage_1": "Ты вошли в лес грибов с большими шляпками и видите дрочущего монстра. Что будешь делать?\n1. Помочь кончить\n2. Убежать нахуй",
        "stage_2": "После того как монстр кончил он указал тебе странную дорогу.  Что будешь делать?\n1. Пойдешь по странной дороге\n2. Убежать в страхе домой",
        "stage_3": "Ты идешь по тропинке и видишь как 13 гномов ебут барана.  Что будешь делать?\n1. Помочь барашке и избить этих уебков\n2. Резко запрыгнуть на баран и ускакать от них обратно домой",
        "stage_4": "Барашка привел тебя к великому Рамзану Кадырову.  Что будешь делать?\n1. Выслушать его",
        "stage_5": "Вы выслушали его величество и он поручил вам украсать золтую овечку.  Что будешь делать?\n1. Выполнить приказ\n2. Ослушаться и получить наказание",
        "stage_6": "Ты добираешься до скрытой долины под названием 'Пидрильщина'  Что будешь делать?\n1. Найти золотую овечку\n2. Сбежать и сохранить себе жизнь",
        "stage_7": "Ты находишь странный храм который охраняет 15 чеченцев.  Что будешь делать?\n1. Найти вход который никто не охраняет\n2. Побежать на пролом",
        "stage_8": "Ты нашел вход и вошел с черного входа, ты сразу увидел как какойто мужчина обнимает золотую овечку.  Что будешь делать?\n1. Окуратно подойдешь сзади и оглушишь мужчину взять овечку и убежать\n2. Подойдешь сзади и задушишь мужчину взять овечку и убежать",
        "stage_9": "Ты успешно украл овечку но мужчина из последних сил крикнул чечнцам что вы украли его жену.  Что будешь делать?\n1. Побежишь через дорогу которая кишит пауками и прибежишь к царю\n2. Побежишь через дорогу которая кишит бешеными собаками и оставь все себе",
        "end_win": "Поздравляем, вы выиграли!",
        "end_lose": "Конец игры, ты умер."
    },
    "en": {
        "start": "You are walking down the street and come across a fork. What will you do?\n1. Go down the path\n2. Turn around and go home",
        "stage_1": "You enter a mushroom forest with large caps and see a monster masturbating. What will you do?\n1. Help him finish\n2. Run away",
        "stage_2": "After the monster finishes, he points you to a strange path. What will you do?\n1. Follow the strange path\n2. Run away to the large mushrooms",
        "stage_3": "You walk down the path and see 13 gnomes having sex with a ram. What will you do?\n1. Help the ram and beat up the gnomes\n2. Quickly jump on the ram and escape back home",
        "stage_4": "The ram leads you to the great Ramzan Kadyrov. What will you do?\n1. Listen to him",
        "stage_5": "You have listened to his majesty and he has tasked you with capturing a golden sheep. What will you do?\n1. Carry out the order\n2. Disobey and face punishment",
        "stage_6": "You arrive at a hidden valley called 'Pidrilshchina'. What will you do?\n1. Find the golden sheep\n2. Flee and save your life",
        "stage_7": "You find a strange temple guarded by 15 Chechens. What will you do?\n1. Find an unguarded entrance\n2. Charge through",
        "stage_8": "You found the entrance and went in through the back, where you immediately saw a man hugging the golden sheep. What will you do?\n1. Carefully approach from behind, knock out the man, grab the sheep, and run\n2. Approach from behind and strangle the man, grab the sheep, and run",
        "stage_9": "You successfully stole the sheep, but the man, with his last strength, shouted to the Chechens that you stole his wife. What will you do?\n1. Run across the road infested with spiders and get to the king\n2. Run across the road infested with rabid dogs and keep everything for yourself",
        "end_win": "Congratulations, you won!",
        "end_lose": "The game is over, you died."
    }
}


class AdventureGame:
    def __init__(self, language="en"):
        self.stage = 0
        self.language = language
        self.messages = messages

    def start_game(self):
        self.stage = 0
        return self.get_current_stage_message()

    def advance_stage(self, choice):
        print(f"Current stage: {self.stage}, Choice: {choice}")

        if self.stage == 0:
            if choice == "1":
                self.stage = 1
            else:
                return self.end_game()
        elif self.stage == 1:
            if choice == "1":
                self.stage = 2
            else:
                return self.end_game()
        elif self.stage == 2:
            if choice == "1":
                self.stage = 3
            else:
                return self.end_game()
        elif self.stage == 3:
            if choice == "1":
                self.stage = 4
            else:
                return self.end_game()
        elif self.stage == 4:
            if choice == "1":
                self.stage = 5
            else:
                return self.end_game()
        elif self.stage == 5:
            if choice == "1":
                self.stage = 6
            else:
                return self.end_game()
        elif self.stage == 6:
            if choice == "1":
                self.stage = 7
            else:
                return self.end_game()
        elif self.stage == 7:
            if choice == "1":
                self.stage = 8
            else:
                return self.end_game()
        elif self.stage == 8:
            if choice == "1":
                self.stage = 9
            else:
                self.stage = 10
        elif self.stage == 9:
            if choice == "1":
                self.stage = 10
            else:
                return self.end_game()

        if self.stage == 10:
            return self.end_game(win=True)

        print(f"New stage: {self.stage}")
        return self.get_current_stage_message()

    def get_current_stage_message(self):
        stage_messages = {
            0: self.messages[self.language]["start"],
            1: self.messages[self.language]["stage_1"],
            2: self.messages[self.language]["stage_2"],
            3: self.messages[self.language]["stage_3"],
            4: self.messages[self.language]["stage_4"],
            5: self.messages[self.language]["stage_5"],
            6: self.messages[self.language]["stage_6"],
            7: self.messages[self.language]["stage_7"],
            8: self.messages[self.language]["stage_8"],
            9: self.messages[self.language]["stage_9"],
        }
        return stage_messages.get(self.stage, self.messages[self.language]["end_lose"])

    def end_game(self, win=False):
        if win:
            return self.messages[self.language]["end_win"]
        else:
            return self.messages[self.language]["end_lose"]

games = {}  # Словарь для отслеживания текущих игр для каждого игрока

@bot.command(name="start")
async def start(ctx, lang="en"):
    if lang not in messages:
        await ctx.send("Can't find this language. Supported languages are: 'en', 'ru'.")
        return
    game = AdventureGame(language=lang)
    games[ctx.author.id] = game
    await ctx.send(game.start_game())

@bot.command(name="continue")
async def continue_game(ctx, choice):
    game = games.get(ctx.author.id)
    if game:
        response = game.advance_stage(choice)
        await ctx.send(response)
    else:
        await ctx.send("You haven't started a game yet. Use `$start` to begin.")

# FIRST GAME

# SECOND GAME (cywe)

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

# lAST EASIEST mini-game
@bot.command(name="flip")
async def flip(ctx):
    outcome = random.choice(["Heads", "Tails"])
    await ctx.send(f"{outcome}")

# lAST EASIEST mini-game

bot.run(token_ds)