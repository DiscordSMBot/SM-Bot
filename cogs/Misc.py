import discord
from discord.ext import commands
import asyncio


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["whois", "UserInfo", "userInfo", "USERINFO", "Userinfo"])
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                              title=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)

        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
        embed.add_field(name="Highest Role:", value=member.top_role.mention)
        print(member.top_role.mention)
        await ctx.send(embed=embed)

    @commands.command(pass_context = True , aliases=['Ping', 'piNg'])
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command()
    async def update(self, ctx):
        embed = discord.Embed(title="Leaf.py Update Log",
                              description="Please specify which version you would like the log of - \n For update 0.1 use ``` Update0_1``` \n For Update 0.2 use ```Update0_2```",
                              color=0xf2da80)
        await ctx.send(embed=embed)

    @commands.command()
    async def Update0_1(self, client, ctx):
        embed = discord.Embed(title="Leaf.py Update 0.1",
                              description="Below is the log for this update: \n ``` New Nickname Command \n Revised Kick, Ban and Unban Commands \n Added embed messages \n Added a Mute command \n Added and AFK command \n Custom Help Command```",
                              color=0xf2da80)
        await ctx.send(embed=embed)
        message = await ctx.send("test")
        await message.add_reaction("◀️")
        await message.add_reaction("▶️")

    @commands.command(pass_context = True , aliases=['Afk', 'aFk'])
    async def afk(self, ctx, mins):
        current_nick = ctx.author.nick
        await ctx.send(f"```{ctx.author.mention} has gone afk for {mins} minutes.```")
        await ctx.author.edit(nick=f"{ctx.author.name} [AFK]")

        counter = 0
        while counter <= int(mins):
            counter += 1
            await asyncio.sleep(60)

            if counter == int(mins):
                await ctx.author.edit(nick=current_nick)
                await ctx.send(f"{ctx.author.mention} is no longer AFK")
                break

    @commands.command()
    async def ver(self, ctx):
        user = ctx.author
        role = discord.utils.get(ctx.guild.roles, name='Verified')
        await user.add_roles(role)
        await ctx.send(f"@{user}, you have been verified! Enjoy your tine here")

    @commands.command()
    async def invite(self, ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=762820891725398067&permissions=8&scope=bot")

def setup(client):
    client.add_cog(Misc(client))
