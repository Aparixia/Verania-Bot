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
    if message.content == ('!cookie'):
        await client.send_message(message.channel, ":cookie:")
    else:
            if message.content == "!group":
                await client.send_message(message.author, "https://www.roblox.com/My/Groups.aspx?gid=3640557")
            else:
                    if message.content == "!holo":
                        await client.send_message(message.author, "https://www.roblox.com/games/1224078932/ZV-Blizzark")
                    else:
                        if message.content == "!rally":
                            await client.send_message(message.author, "https://www.roblox.com/games/1224110579/ZV-Operation-Overdrive")
                        else:
                            if message.content == "!fort":
                                await client.send_message(message.author, "https://www.roblox.com/games/1224113519/ZV-Storm-Peak")
                            else:
                                if message.content == "!ad":
                                    await client.send_message(message.author, "https://www.roblox.com/games/1263970819/ZV-Auto-Duels")
                                else:
                                    if message.content == "!grp":
                                        await client.send_message(message.author, "https://www.roblox.com/games/6194809/Group-Recruiting-Plaza")
                                    else:
                                         if message.content == "!greet":
                                             userID = message.author.id
                                             await client.send_message(message.channel, "Hello, <@%s>!" % (userID))
                                         else:
                                                if message.content == "yip yip":
                                                   await client.delete_message(message)
                                                else:
                                                     if message.content == "!help":
                                                         await client.send_message(message.author,
                                                      "                                                                                                                                                                                                                                 Verania Bot V.1.0.3"
                                                      "                                                                                                                                                                                                                                                                          . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         "                
                                                      "                                                                                                                                                                                                                                 Created by Grand General Aparixia."
                                                      "                                                                                                                                                                                                                                                                          . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         "                                  
                                                      "                                                                                                                                                                                                                                 https://pastebin.com/raw/svCTCmGR"
                                                      "                                                                                                                                                                                                                                                                           . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       "
                                                      "                                                                                                                                                                                                                                 Say !info for more information.")
                                                         msg = await client.wait_for_message(author=message.author, content='!info')
                                                         await client.send_message(message.author, "Specifically for chat-based problems and an overall unique server, Verania is a Python-scripted bot that serves Zone Verona. Got any questions or concerns? DM Spooky Ghost#4720 !")
                                                     else:
                                                            if message.content.upper().startswith('!SAY'):
                                                                 if message.author.id == "285384820392198145":
                                                                    await client.delete_message(message)
                                                                    args = message.content.split(" ")
                                                                    await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
                                                                 else:
                                                                    if message.content.upper().startswith('!SAY'):
                                                                         if message.author.id == "393753000616656897":
                                                                            await client.delete_message(message)
                                                                            args = message.content.split(" ")
                                                                            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
                                                                         else:
                                                                           if message.content.upper().startswith('!SAY'):
                                                                                 if message.author.id == "278907050862313472":
                                                                                    await client.delete_message(message)
                                                                                    args = message.content.split(" ")
                                                                                    await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
                                                                                 else:
                                                                                    msg = await client.wait_for_message(author=message.author, content='192837192387123871293871092837190283712938719238719082730918273')
        

client.run("Mzk2NzIzMjg5NzgwNzgxMDU3.DSllwQ.mhmNiUbHT5_ohtBV-9WGZvKYaoY")
                                
