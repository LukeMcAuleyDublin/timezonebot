import os
import discord
import responses
import tz
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(intents = intents, command_prefix="!")

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')

    @bot.command(name='ping', help='Plays ping pong!')
    async def ping(ctx):
        await ctx.send('Pong!')

    @bot.command(name='timezone', help='displays various timezones')
    async def timezone(ctx):
        message = tz.timezones()
        await ctx.send(message)

    @bot.command(name='addtimezone', help='adds a timezone to the list of timezones to display')
    async def addtimezone(ctx):
        tz.user_timezones.append(ctx.message.content)
    bot.run(TOKEN)