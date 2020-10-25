import discord
from discord import Embed
from discord.ext import commands, tasks
import json
import os
import datetime
from random import randint
from discord.utils import get



class Posts(commands.Cog):

    def __init__(self, client):
        self.client = client

    def message_log(client, channel):
        with open('log.json', 'r') as f:
            logs = json.load(f)

        return logs[str(channel.guild.id)]

    @commands.command()
    async def setup_counter(self, ctx, gd = 0):
        guild = self.client.get_guild(gd)  # <-- insert yor guild id here
        await ctx.send("Setting up management!")
        category = await guild.create_category("Management", overwrites=None, reason=None)
        await guild.create_voice_channel(f"Member Count:", overwrites=None, category=category,
                                         reason=None)
        await ctx.send("Setup finished!")

    @commands.command()
    async def testing(self, ctx):
        await ctx.channel.send("Please confirm")

        def check(m):
            return m.content.lower() == "confirm" and m.author == ctx.message.author

        await self.client.wait_for('message', check=check, timeout=10)
        # HOW TO DELETE THE INITIAL MESSAGE SENT BY THE BOT
        await ctx.bot.logout()

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        with open('log.json', 'r') as f:
            logs = json.load(f)

        Channel = logs[str(message.guild.id)]
        Ch = int(Channel)

        channel = self.client.get_channel(Ch)
        embed = discord.Embed(description=f"Message deleted in {message.channel.mention}", color=0x4040EC).set_author(name=message.author, url=Embed.Empty, icon_url=message.author.avatar_url)
        embed.add_field(name="Message", value=message.content)
        embed.timestamp = message.created_at
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(Posts(client))