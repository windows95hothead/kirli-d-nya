import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(description='Başka yönden skor yapsana')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))  
@bot.command()
async def topla(ctx,sayı =0,sayı2=0):
    x=sayı+sayı2
    await ctx.send(f"verdiğiniz sayıların toplamı {x} tir")
@bot.command()
async def peh(ctx, count_peh = 1):
    await ctx.send("pehleme aptal" * count_peh)
@bot.command()
async def mem(ctx):
    deg = os.listdir("img")
    rastgelemem = random.choice(deg)
    with open(f'img/{rastgelemem}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

bot.run("MTIxNTk1NjI2OTQ0NjQ2MzU2OQ.GRco0U.7FULSyKCYM_hUzr55p3wlm5aWl5c8Q-ZHITLV4")


