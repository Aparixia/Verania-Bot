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
          if message.content == "Shout Training": 
             if message.author.id == ("285384820392198145"):
                 await client.delete_message(message)
                 await client.send_message(message.channel, "@here TRAIN | Training will be hosted by Aparixia and will occur at the Blizzark Facility. Join here! https://www.roblox.com/games/1224078932/ZV-Blizzark ")
             else:
                  await client.send_message(message.channel, "You do not have permission to run this command.")
            
@client.event 
async def on_message(message):
          if message.content == "End Training": 
             if message.author.id == ("285384820392198145"):
                 await client.delete_message(message)
                 await client.send_message(message.channel, "TRAIN | Over. -Grand General")
             else:
                  await client.send_message(message.channel, "You do not have permission to run this command.")
            

client.run("Mzk2NzIzMjg5NzgwNzgxMDU3.DSllwQ.mhmNiUbHT5_ohtBV-9WGZvKYaoY")






#("393753000616656897")("278907050862313472")("207343854872035328")("305784064919732225")("206013134127759361")("364079081819602944")("277242005774663683")("356226749417390080")("261203386333003778")
