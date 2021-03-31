#imports
import os
import math
import random
import discord
import youtube_dl
import asyncio
from asyncio import sleep as s
from discord.ext import commands
from discord import FFmpegPCMAudio as ff
from dotenv import load_dotenv

#custom imports
import bot_messages
import bot_db as db
from games import gamble
import lottery.controller as lotto

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='p!',help_command=None)

@bot.event
async def on_ready():
    print("ready!")

@bot.event
async def on_message(message):

    channel = message.channel

    if not message.author.bot:
        if 'eyes' in message.content.lower():
            print(message.content)
            await channel.send(':eyes:')

    await bot.process_commands(message)

@bot.event
async def on_member_join(member):

    chan = await member.create_dm()

    await chan.send(
        f'Welcome to the server {member.name}, feel free to munch on bamboo while you await others. :bamboo:'
    )

    print("Panda Bot sent a user a DM")

@bot.command(name="help")
async def help(ctx):
    # Creates a help command
    embed = discord.Embed(title="Panda Bot Help",description="Panda Bot for Dummies.")
    #embed.color = "red"
    embed.add_field(name="p!Help", value="Shows this table!")
    embed.add_field(name="p!echo", value="I'll repeat whatever you say. Don't make it dirty please. D:")
    embed.add_field(name="p!howispanda",value="Ask how I am. :)")
    embed.add_field(name="p!pokemon", value="I'll respond with a random quote or funny line from Pokemon!")
    embed.add_field(name="p!roll", value="One dice roll coming up! Specify the sides like: 'p!roll 6'")

    embed2 = discord.Embed(title="Panda Gambling Help",description="Don't blow all of your money!")
    embed2.add_field(name="p!gamble highlow 'amount to bet' 'high or low'",value="")

    await ctx.send(content=None,embed=embed+embed2)

@bot.command(name="echo",help="I'll repeat whatever you say, but don't make it dirty please. D:")
async def echo(ctx,str):
    if str:
        await ctx.send(str)
    else:
        await ctx.send("Hmm, couldn't hear you, speak up!")
    
@bot.command(name="roll",help="I'll a die for you, put the sides after the command like: !roll 6")
async def rolld(ctx, sides: int):
    await ctx.send(random.choice(range(1,sides)))

@bot.command(name="howispanda",help="I wonder how he is doing...")
async def how_is_panda(ctx):
    response = random.choice(bot_messages.day)

    await ctx.send(response)

@bot.command(name="pokemon",help="Says a random Pokemon quote!")
async def pokemon(ctx):
    response = random.choice(bot_messages.pokemon)

    await ctx.send(response)

# Point Gambling
@bot.command(name="lotto",help="Each ticket costs 100 points, we draw on friday!")
async def addToLotto(ctx, points:int):
    uid = ctx.message.author.id
    if db.get_points(uid) >= points:
        db.change_points(uid,100*(math.floor(points/100)),"sub")
        lotto.addTicket(ctx.message.author.name, uid, points)
    await ctx.send(f"You've bought {math.floor(points/100)} tickets!.")


@bot.command(name="creategambler",help="Creates a gambling profile for you to gamble fake money! Yay!")
async def create_gam(ctx):

    status = db.new_user(ctx.message.author.name,ctx.message.author.id)

    if status == True:
        await ctx.send("User Created, start gambling! You get 100 to start. :)")
    else:
        await ctx.send("You already have a gambling profile!")

@bot.command(name="getpoints",help="I'll let you know how many points you have")
async def get_points(ctx):

    await ctx.send(f'You have: {db.get_points(ctx.message.author.id)}')

@bot.command(name="gamble")
async def game(ctx, game, amount:int, bet):
    print(game, amount, bet)

    user_points = db.get_points(int(ctx.message.author.id))

    if user_points < amount:
        await ctx.send(f'You bet more than you have! You currently have {user_points}, you bet {amount}.')

    elif game == "highlow" and db.get_points(int(ctx.message.author.id)) >= amount:

        result,total,d1,d2 = gamble.hi_low()
        await ctx.send(f'The result was {result}, total face value of dice was {total}, and dice faces were, {d1},{d2}')

        if result == bet.lower():
            await db.change_points(int(ctx.message.author.id),amount,"add")
        else:
            await db.change_points(int(ctx.message.author.id),amount,"sub")

    elif game =="evensodds" and db.get_points(int(ctx.message.author.id)) >= amount:

        result,total = gamble.odds_evens()
        if result == bet.lower():
            db.change_points(int(ctx.message.author.id),amount,"add")
            await ctx.send(f'You guessed right! The dice face was {total}, it was {result}!')
        else:
            db.change_points(int(ctx.message.author.id),amount,"sub")
            await ctx.send(f'You guessed wrong! The dice face was {total}, it was {result}!')

# Audio client commands

@bot.command(name="join")
async def join(ctx):
    if ctx.author.voice:
        voiceChannel = ctx.message.author.voice.channel
        print(voiceChannel)
        #voice = discord.utils.get(bot.voice_clients,guild=ctx.guild)
        voice = await voiceChannel.connect()
        source = ff('KillingTime.m4a')
        voice.play(source)
        return

    await ctx.send(f'You are not in a voice channel, {ctx.author.name}. I do not know you well enough to go to your house, yet... :eyes:')
    
@bot.command(name="pause")
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients,guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.guild.me.edit(nick='Panda Bot(Paused)')
        await ctx.send(f'Audio is resumed in channel {ctx.message.author.voice.channel.name}. Resume with "p!resume"' )
        return
    await ctx.send(f'There is no audio playing, invite me to a channel first. :bamboo:')

@bot.command(name='resume')
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients,guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        return
    await ctx.send(f'The sound is either already paused, or there is nothing playing.')
    

@bot.command(name="leave")
async def leave(ctx):
    await ctx.voice_client.disconnect()

# admin commands:
@bot.command(name="setuplotto")
@commands.has_role("Admin")
async def setupLotto(ctx):
    while True:
        await s(60)
        await ctx.send("Waited")

@bot.command(name="givemepoints")
@commands.has_role("Admin")
async def give_me_points(ctx,a:int):
    userid=int(ctx.message.author.id)
    db.change_points(userid,a,"add")
    await ctx.send(f'Added {a} to your banking account, {ctx.message.author.name}.')

@bot.command(name="createchannel")
@commands.has_role("Admin")
async def create_channel(ctx,channel_name):
    guild = ctx.guild
    if not discord.utils.get(guild.channels, name=channel_name):
        print(f'Creating Channel: {channel_name}')
        await guild.create_text_channel(channel_name)

# error handling:
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.errors.CheckFailure):
        await ctx.send("You don't have permission to change the bamboo forest!")

# @bot.event
# async def on_error(event, *args, **kwargs):
#     with open("err.log", "a") as f:
#         if event == "on_message":
#             f.write(f'Unhandled error: {args[0]}\n')

bot.run(TOKEN)