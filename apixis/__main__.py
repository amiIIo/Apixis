import discord

with open("./secrets/token") as f:
    token = f.read().strip()

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Not to fear, Apixis is here!")

bot.run(token)