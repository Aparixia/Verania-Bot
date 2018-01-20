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
                                                if message.content == "!fallen":
                                                    await client.send_message(message.channel, "<@FallenElectron#4773> is a gay bastard.")
                                                else:
                                                     if message.content == "!info":
                                                         await client.send_message(message.author,"Verania Bot Ver. 2.1")
                                                         await client.send_message(message.author,"Created by Luminary Aparixia.")
                                                         await client.send_message(message.author,"═════════════════════════════")
                                                         await client.send_message(message.author,"COMMANDS")
                                                         await client.send_message(message.author,"!info - Displays this dialogue prompt in Direct Messages.")
                                                         await client.send_message(message.author,"!group - Sends you a link to Zone Verona in Direct Messages.")
                                                         await client.send_message(message.author,"!holo - Sends you a link to the Zone Verona HOLO in Direct Messages.")
                                                         await client.send_message(message.author,"!rally - Sends you a link to the Zone Verona Rally in Direct Messages.")
                                                         await client.send_message(message.author,"!fort - Sends you a link to the Zone Verona Fort in Direct Messages.")
                                                         await client.send_message(message.author,"!grp - Sends you a link to Group Recruiting Plaza in Direct Messages.")
                                                         await client.send_message(message.author,"!cookie - Displays a :cookie: for you!")
                                                         await client.send_message(message.author,"!greet - Greets the sender.")
                                                     else:
                                                         msg = await client.wait_for_message(author=message.author, content='192837192387123871293871092837190283712938719238719082730918273')
        

client.run("NDAzMjkxMTg2NTczNDc1ODQw.DUS55Q.lPBnPbwzUc5Bj9oniyg6ZnlnRww")
                                
