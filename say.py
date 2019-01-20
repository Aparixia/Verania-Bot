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
         
# Message Commands

@client.event
async def on_message(message):
    
    if message.content == ('+cookie'):
        userID = message.author.id
        await client.send_message(message.channel, "Here is a :cookie: for you, <@%s>!" % (userID))
             
# Verify System

    if message.content == ('+verify'):
        user = await client.get_user_info('349232253672357890')
        author = message.author
        await client.send_message(author, 'Welcome! Please state your rank.')
        msg = await client.wait_for_message(author=message.author)
        await client.send_message(author, 'Your response has been sent to a High Rank. You will be ranked soon!')
        args = msg.content
        await client.send_message(user, '%s is ready to be roled and ranked to:' % (author))
        await client.send_message(user, args)

# Fun Commands

    if message.content == ('+greet'):
        userID = message.author.id
        await client.send_message(message.channel, "Hi, **<@%s>**!" % (userID))

    if message.content.upper().startswith('!HUG'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "**Chasma** hugs **%s**! :heart:" % (" ".join(args[1:])))
        
    if message.content.upper().startswith('!HIT'):

        await client.send_message(message.channel, "**Chasma** smacks **%s**! :hand_splayed:" % (" ".join(args[1:])))
        
    if message.content.upper().startswith("!RATE"):
        randomnum = random.randint(0, 10)
        await client.send_message(message.channel, "I'd rate that with a &s out of 10." % (randomnum))

# RPS

    
    elif message.content.startswith("!rps"):
        await client.send_message(message.channel, "Alright! What do you pick?")
        answer = await client.wait_for_message(author=message.author)
        randomnum = random.randint(0, 2)
        if randomnum == 0:
            if answer.content.upper().startswith('!ROCK'):
               await client.send_message(message.channel, "Paper! I win! :hand_splayed:")
            else:
                if answer.content.upper().startswith('!SCISSORS'):
                    await client.send_message(message.channel, "Paper! You win! :hand_splayed:")
                else:
                    if answer.content.upper().startswith('!PAPER'):
                        await client.send_message(message.channel, "Paper! We tie! :hand_splayed:")
                    else:
                        await client.send_message(message.channel, "Did you say the right command?")
        else:                 
            if randomnum == 1:
                if answer.content.upper().startswith('!ROCK'):
                   await client.send_message(message.channel, "Scissors! You win! :v:")
                else:
                    if answer.content.upper().startswith('!SCISSORS'):
                        await client.send_message(message.channel, "Scissors! We tie! :v:")
                    else:
                        if answer.content.upper().startswith('!PAPER'):
                            await client.send_message(message.channel, "Scissors! I win! :v:")
                        else:
                           await client.send_message(message.channel, "Did you say the right command?")
            else:
                if randomnum == 2:
                    if answer.content.upper().startswith('!ROCK'):
                       await client.send_message(message.channel, "Rock! We tie! :fist:")
                    else:
                        if answer.content.upper().startswith('!SCISSORS'):
                            await client.send_message(message.channel, "Rock! I win! :fist:")
                        else:
                            if answer.content.upper().startswith('!PAPER'):
                                await client.send_message(message.channel, "Rock! You win! :fist:")
                            else:
                                await client.send_message(message.channel, "Did you say the right command?")




        if message.content.upper().startswith("!rate"):
             args = message.content.split(" ")
             randomnum = random.randint(1, 10)
             if randomnum == 1:
                await client.send_message(message.channel, "I'd give **%s** a **1/10**. :frowning:" % (" ".join(args[1:])))
             else:
                 if randomnum == 2:
                    await client.send_message(message.channel, "I'd give **%s** a **2/10**. :frowning:" % (" ".join(args[1:]))) 
                 else:
                    if randomnum == 3:
                        await client.send_message(message.channel, "I'd give **%s** a **3/10**. :frowning:" % (" ".join(args[1:])))

                    else:
                        if randomnum == 4:
                            await client.send_message(message.channel, "I'd give **%s** a **4/10**. :slight_frown:" % (" ".join(args[1:])))
                     
                        else:
                            if randomnum == 5:
                                await client.send_message(message.channel, "I'd give **%s** a **5/10**. :neutral_face:" % (" ".join(args[1:])))

                            else:
                                if randomnum == 6:
                                    await client.send_message(message.channel, "I'd give **%s** a **6/10**. :slight_smile:" % (" ".join(args[1:])))

                                else:
                                    if randomnum == 7:
                                        await client.send_message(message.channel, "I'd give **%s** a **7/10**. :slight_smile:" % (" ".join(args[1:])))

                                    else:
                                        if randomnum == 8:
                                            await client.send_message(message.channel, "I'd give **%s** a **8/10**. :smile:" % (" ".join(args[1:])))

                                        else:
                                            if randomnum == 9:
                                                await client.send_message(message.channel, "I'd give **%s** a **9/10**. :smile:" % (" ".join(args[1:])))

                                            else:
                                                if randomnum == 10:
                                                    await client.send_message(message.channel, "I'd give **%s** a **10/10**. :smile:" % (" ".join(args[1:])))

                                        
# Boring Commands
   
    if message.content == ('+status'):
        await client.send_message(message.channel, message.author.status)

    if message.content == ('+game'):
        await client.send_message(message.channel, message.author.game)

    if message.content == ('+joined'):
        await client.send_message(message.channel, message.author.joined_at)
        
    if message.content == ('+toprole'):
        await client.send_message(message.channel, message.author.top_role)

    if message.content == ('+color'):
        await client.send_message(message.channel, message.author.color)

# Group Links
   
    if message.content == "!group":
        await client.send_message(message.author, "https://www.roblox.com/my/groups.aspx?gid=4100568")

    if message.content == "!holo":
        await client.send_message(message.author, "https://www.roblox.com/games/1716492386/EA-Flagship-Metuo")

    if message.content == "!fort":
        await client.send_message(message.author, "https://www.roblox.com/games/1946723603/EA-Battleship-Lietus")
                                    
                                                
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
    await client.send_message(member, "Welcome to Ethereal Abyss! Make sure to say +verify to get roled.")
  
# Bot Token           

client.run("NDA3MTMxNTc1NDQ5Mjg4NzA0.DU9Cfw.xy3asep0_j0Gihg-5uBwqd1Q2Ws")

