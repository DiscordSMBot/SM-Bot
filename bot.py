import discord
from discord.ext import commands
from discord.ext.commands import bot
import os
import json
import asyncio
import random
from discord.utils import get
import time
from discord import Embed

intents = discord.Intents.default()
intents.members = True


#-----------json file control-----------#

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

def message_log(client, channel):
    with open('log.json', 'r') as f:
        logs = json.load(f)

    return logs[str(channel.guild.id)]

def welcome(client, welcome):
    with open('welcome.json', 'r') as f:
        welcomes = json.load(f)

    return welcomes[str(welcome.guild.id)]

def welcomem(client, welcome):
    with open('welcomem.json', 'r') as f:
        welcomesm = json.load(f)

    return welcomesm[str(welcome.guild.id)]

#-----------Client control-----------#

client = commands.Bot(command_prefix = get_prefix, intents=intents, case_insensitive=False)

owner = "141695444995670017"

client.remove_command("help")

client.status = "Change"

#-----------Defualt Events-----------#

@client.event
async def on_ready():
    print("--------------")
    print("|            |")
    print("|            |")
    print("|            |")
    print("-------------")

@client.event
async def on_member_join(member):
    with open('welcome.json', 'r') as f:
        welcomes = json.load(f)

    welcomes[str(member.guild.id)]

    Channel = welcomes[str(member.guild.id)]
    Ch = int(Channel)
    channel = client.get_channel(Ch)

    await channel.send(f"Hey @{member}, thanks for joining {member.guild.name}, enjoy your time!")


@client.event
async def on_guild_join(guild):

    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '>'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    with open('log.json', 'r') as f:
        logs = json.load(f)

    logs[str(guild.id)] = ''

    with open('log.json', 'w') as f:
        json.dump(logs, f, indent=4)
#----------------------------------
    with open('welcome.json', 'r') as f:
        welcomes = json.load(f)

    welcomes[str(guild.id)] = ''

    with open('welcome.json', 'w') as f:
        json.dump(welcomes, f, indent=4)

    with open('welcomem.json', 'r') as f:
        welcomesm = json.load(f)

    welcomesm[str(guild.id)] = f'Hey, please welcome the new member to the server!'

    with open('welcomem.json', 'w') as f:
        json.dump(welcomesm, f, indent=4)




#-----------Needed commands-----------#

@client.command(pass_context=True, aliases=['prefix'])
async def Prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def insdsxsfo(ctx):
    embed = discord.Embed(title="Leaf.py",
                          description=f"Leaf.py is a fully functional and powerful bot! It offers a variaty of features which can not be found with other bots! \n **Guilds:**ㅤㅤㅤㅤㅤㅤㅤㅤ**Version:** \n  12ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ0.1  \n \n **Status:** {client.status}",
                          color=0xf2da80)
    await ctx.send(embed=embed)

@client.command()
async def inffsdxcostatus(ctx, *, status: str):
    client.status = status

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} Unloaded!')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} Reloaded!')

@client.command()
@commands.is_owner()
async def load(ctx, extension):
     client.load_extension(f'cogs.{extension}')
     await ctx.send(f'{extension} Loaded!')

#-----------Commands being tested-----------#

@client.command(pass_context=True, aliases=['Setmlog'])
@commands.has_permissions(manage_roles=True)
async def setmlog(ctx, cha):
    with open('log.json', 'r') as f:
        logs = json.load(f)

    logs[str(ctx.guild.id)] = cha

    with open('log.json', 'w') as f:
        json.dump(logs, f, indent=4)

@client.command(pass_context=True, aliases=['Setwelcome'])
@commands.has_permissions(manage_roles=True)
async def setwelcome(ctx, cha):
    with open('welcome.json', 'r') as f:
        welcomes = json.load(f)

    welcomes[str(ctx.guild.id)] = cha

    with open('welcome.json', 'w') as f:
        json.dump(welcomes, f, indent=4)

@client.command()
@commands.has_permissions(manage_roles=True)
async def setwelcomemessage(ctx, cha):
    with open('welcomem.json', 'r') as f:
        welcomesm = json.load(f)

    welcomesm[str(ctx.guild.id)] = cha

    with open('welcomem.json', 'w') as f:
        json.dump(welcomesm, f, indent=4)


extensions = ['cogs.Moderation', 'cogs.Helpcommand', 'cogs.Misc', 'cogs.OW', "cogs.Fun", "cogs.Giveaway", 'cogs.Posts']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)

client.run('NzYyODIwODkxNzI1Mzk4MDY3.X3uuUQ.7ODKUy4yuQadwVlx1JXLk7AffLI')
