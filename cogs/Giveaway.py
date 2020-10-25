import discord
import datetime
import time
import asyncio
import random

from discord.ext import commands
from discord import Embed

class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['Giveaway', 'GiveAway', 'giveAway'])
    async def giveaway(self, ctx, time: int, *, prize):
        giveawayembed = discord.Embed(
            title="🎉 New Giveaway! 🎉",
            colour=discord.Color.green()
        )

        giveawayembed.add_field(name="Prize", value="{}".format(prize), inline=False)
        giveawayembed.add_field(name="Hosted by", value=f"{ctx.author.mention}", inline=False)
        giveawayembed.add_field(name="Ends in", value="{}s".format(time))

        msg = await ctx.send(embed=giveawayembed)

        await msg.add_reaction("🎉")

        await asyncio.sleep(time)

        msg = await msg.channel.fetch_message(msg.id)
        winner = None

        for reaction in msg.reactions:
            if reaction.emoji == "🎉":
                users = await reaction.users().flatten()
                users.remove(self.client.user)
                winner = random.choice(users)

        if winner is not None:
            endembed = discord.Embed(
                title="Giveaway ended!",
                description="Prize: {}\nWinner: {}".format(prize, winner))

            await msg.edit(embed=endembed)

    @giveaway.error
    async def giveaway_error(self, ctx, error):
        await ctx.send(error)
        print(error)
        raise error

def setup(client):
    client.add_cog(Giveaway(client))




