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

# Verify System

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

# Fun Commands

    if message.content == ('!greet'):
        userID = message.author.id
        await client.send_message(message.channel, "Hi, **<@%s>**!" % (userID))

    if message.content.upper().startswith('!HUG'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "**Sennzai** hugs **%s**! :heart:" % (" ".join(args[1:])))
        
    if message.content.upper().startswith('!HIT'):

        await client.send_message(message.channel, "**Sennzai** smacks **%s**! :hand_splayed:" % (" ".join(args[1:])))
        
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
                                       
# Boring Commands
   
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

# Group Links
   
    if message.content == "!group":
        await client.send_message(message.author, "https://www.roblox.com/My/Groups.aspx?gid=3640557")

    if message.content == "!holo":
        await client.send_message(message.author, "https://www.roblox.com/games/1224078932/ZV-Blizzark")

    if message.content == "!rally":
        await client.send_message(message.author, "https://www.roblox.com/games/1224110579/ZV-Operation-Overdrive")

    if message.content == "!fort":
        await client.send_message(message.author, "https://www.roblox.com/games/1224113519/ZV-Storm-Peak")

    if message.content == "!ad":
        await client.send_message(message.author, "https://www.roblox.com/games/1263970819/ZV-Auto-Duels")
                           
    if message.content == "!grp":
        await client.send_message(message.author, "https://www.roblox.com/games/6194809/Group-Recruiting-Plaza")
                                    
    if message.content == "!greet":
        userID = message.author.id
        await client.send_message(message.channel, "Hello, <@%s>!" % (userID))
                                                
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
    await client.send_message(member, "Welcome to Zone Verona! Remember to read the rules to have the best experience here. Say !verify to get begin the roling prompt.")
  
# Bot Token           

client.run("NDA3MTMxNTc1NDQ5Mjg4NzA0.DU9Cfw.xy3asep0_j0Gihg-5uBwqd1Q2Ws")

