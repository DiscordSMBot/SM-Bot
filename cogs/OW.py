import discord
from discord.ext import commands
import inspect



class OW(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def Status_Update(self, ctx, *, status="Defualt Prefix = >"):
        game = discord.Game(status)
        await self.client.change_presence(status=discord.Status.online, activity=game)
        print(status)
        if commands.is_owner == False:
            embed = discord.Embed(title="Error", description="This command is an Owner Only command")
            await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.bot.logout()

def setup(client):
    client.add_cog(OW(client))
