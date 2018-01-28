import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

# Startup & Presence Changer

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
    print("Bot is online and connected to Discord.")
    await client.change_presence(game=discord.Game(name='with Magic!'))
         
# Message Commands

@client.event
async def on_message(message):
    
    if message.content == ('!cookie'):
        userID = message.author.id
        await client.send_message(message.channel, "Here is a :cookie: for you, <@%s>!" % (userID))

    
    if message.content == ('!info'):
        await client.send_message(message.author, "Hi, I'm Sennzai!")
        await client.send_message(message.author, "``!cookie - Gives you a cookie!``")
        await client.send_message(message.author, "``!greet - Greets the sender!``")
        await client.send_message(message.author, "``!hug (name) - Hugs the chosen person!``")
        await client.send_message(message.author, "``!status - Displays your current status.``")
        await client.send_message(message.author, "``!game - Displays the game you are currently playing.``")
        await client.send_message(message.author, "``!joined - Displays the time and date of when you joined.``")
        await client.send_message(message.author, "``!toprole - Displays your highest ranking role.``")
        await client.send_message(message.author, "``!color - Displays the showing color of your role.``")
             

    if message.content == ('!verify'):
        user = await client.get_user_info('349232253672357890')
        emperor = await client.get_user_info('393753000616656897')
        author = message.author
        await client.send_message(author, 'Welcome! Please state your rank.')
        msg = await client.wait_for_message(author=message.author)
        await client.send_message(author, 'Your response has been sent to a High Rank. You will be ranked soon!')
        args = msg.content
        await client.send_message(user, '%s is ready to be roled and ranked to:' % (author))
        await client.send_message(user, args)
        await client.send_message(emperor, '%s is ready to be roled and ranked to:' % (author))
        await client.send_message(emperor, args)

    if message.content == ('!greet'):
        userID = message.author.id
        await client.send_message(message.channel, "Hi, **<@%s>**!" % (userID))

    if message.content.upper().startswith('!HUG'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "**Sennzai** hugs **%s**! :heart:" % (" ".join(args[1:])))
   
    if message.content == ('!status'):
        await client.send_message(message.channel, message.author.status)

    if message.content == ('!game'):
        await client.send_message(message.channel, message.author.game)

    if message.content == ('!joined'):
        await client.send_message(message.channel, message.author.joined_at)
        
    if message.content == ('!toprole'):
        await client.send_message(message.channel, message.author.top_role)

    if message.content == ('!color'):
        await client.send_message(message.channel, message.author.color)
        
# Censoring System

    if "yip" in message.content.lower():
         await client.delete_message(message)

    if "nigga" in message.content.lower():
         await client.delete_message(message)

    if "nigger" in message.content.lower():
         await client.delete_message(message)


# Welcome System

@client.event
async def on_member_join(member):
    await client.send_message(member, "Welcome to Zone Verona! Remember to read the rules to have the best experience here. Say !verify to get being the roling prompt.")
  
# Bot Token           

client.run("NDA3MTMxNTc1NDQ5Mjg4NzA0.DU9Cfw.xy3asep0_j0Gihg-5uBwqd1Q2Ws")

