#imports
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

#custom imports
import bot_messages
import bot_command_functions as bcf

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='!') 

@bot.event
async def on_ready():
    print("ready!")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Welcome to the server {member.name}, feel free to munch on bamboo while you await others. :bamboo:'
    )
    print("Panda Bot sent a user a DM")

@bot.command(name="echo",help="I'll repeat whatever you say, but don't make it dirty please. D:")
async def echo(ctx,str):
    if str:
        await ctx.send(str)
    
@bot.command(name="roll",help="I'll a die for you, put the sides after the command like: !roll 6")
async def rolld6(ctx, sides: int):
    await ctx.send(random.choice(range(1,sides)))

@bot.command(name="howispanda",help="I wonder how he is doing...")
async def how_is_panda(ctx):
    print("howispanda")
    response = random.choice(bot_messages.day)
    await ctx.send(response)

@bot.command(name="pokemon",help="Says a random Pokemon quote!")
async def pokemon(ctx):
    print("pokemon")
    response = random.choice(bot_messages.pokemon)
    await ctx.send(response)

# admin commands:
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

@bot.event
async def on_error(event, *args, **kwargs):
    with open("err.log", "a") as f:
        if event == "on_message":
            f.write(f'Unhandled error: {args[0]}\n')

bot.run(TOKEN)