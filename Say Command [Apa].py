import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("Bot is online and connected to Discord")


@client.event
async def on_message(message):
    if message.content.upper().startswith('!SAY'):
        if message.author.id == ("285384820392198145"):
            await client.delete_message(message)
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not have permission to run this command.")








client.run("Mzk2NzIzMjg5NzgwNzgxMDU3.DSllwQ.mhmNiUbHT5_ohtBV-9WGZvKYaoY")
