import discord

from discord.ext import commands

intents = discord.Intents.default()  
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

import comandos

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')



# Executando o bot com o token
bot.run('TOKEN')