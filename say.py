import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

# Startup & Presence Changer

Client = discord.Client()
client = commands.Bot(command_prefix = "+")
@client.event
async def on_ready():
    print("Bot is online and connected to Discord.")
    await client.change_presence(game=discord.Game(name='with shutdown clans! | prefix: +'))
                                    
                                                
# Censoring System
async def on_message(message):
    if "yip" in message.content.lower():
         await client.delete_message(message)

    if "nigga" in message.content.lower():
         await client.delete_message(message)

    if "nigger" in message.content.lower():
         await client.delete_message(message)

  
# Bot Token           

client.run("NDA3MTMxNTc1NDQ5Mjg4NzA0.DU9Cfw.xy3asep0_j0Gihg-5uBwqd1Q2Ws")

