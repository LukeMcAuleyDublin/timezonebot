# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.none()
intents.messages = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Hello!')

@bot.command(name='timezones')
async def timezones(ctx):
    await ctx.send('Hello!')

@client.event
async def on_message(message):
    if 'hello' in message.content.lower():
        await message.channel.send('Hello!')

bot.run(TOKEN)