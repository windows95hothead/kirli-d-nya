import discord
import os
from discord.ext import commands
import random
TOKEN = ''
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
kirlilik_mesaji = (
            "Çevre kirliliğini azaltmak için yapabileceğiniz bazı adımlar:\n"
            "1. Atıklarınızı ayrıştırarak geri dönüşüme katkıda bulunun.\n"
            "2. Plastik kullanımını minimumda tutarak çevreye olan etkinizi azaltın.\n"
            "3. Toplu taşımayı tercih ederek karbon ayak izinizi azaltın.\n"
            "4. Enerji tasarruflu ampuller kullanarak enerji tüketiminizi azaltın.\n"
            "5. Daha fazla ağaç dikerek doğal yaşam alanlarını koruyun.\n"
            "6. Atık suyunuzu doğaya zarar vermeyecek şekilde arıtarak kullanın."
        )
async def cevre_mesaj(message):
    kirlilik_mesaji = kirlilik_mesaji
    await message.channel.send(kirlilik_mesaji)
    
    fotolar = os.listdir("çevrekirliliğifoto")
    ratsgele = random.choice(fotolar)
    with open(f'çevrekirliliğifoto/{ratsgele}', 'rb') as f:
        foto = discord.File(f)
        await message.channel.send(file=foto)
@bot.command()
async def kirlilik_azalt(ctx):
    await ctx.send(kirlilik_mesaji)
@bot.command()
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('!kirlilik_azalt'):
        await kirlilik_azalt(message)

bot.run(TOKEN)        