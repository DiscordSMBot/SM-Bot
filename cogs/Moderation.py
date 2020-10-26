import discord
import datetime
import asyncio
import json
import os
import os.path

from discord.ext import commands
from os.path import isfile, join
from os import listdir
from random import randint
from datetime import datetime

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['Mute', 'mUte'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, mute_time: int, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(f'**Muted** {member.mention}\n**Reason: **{reason}\n**Duration:** {mute_time}')

        await asyncio.sleep(mute_time)
        await member.remove_roles(role)
        await ctx.send(f"**Unmuted {member.mention}**")


    #@mute.error
    #async def mute_error(self, ctx, error):
        #if isinstance(error, commands.MissingRequiredArgument):
            #embed = discord.Embed(title="Mute - MODERATION", description="Mute - This command is used to mute users and to prevent them from talking  \n **Main Command** \n `mute <member> ` \n **Sub Commands** \n `None`", timestamp=ctx.message.created_at,  color=0xf2da80)
            #embed.set_footer(text=f"Requested by {ctx.author}")
            #await ctx.send(embed=embed)


    @commands.command(pass_context=True, aliases=['Purge', 'pUrge'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=0):
        embed = discord.Embed(title="Purged", description=f"We purged {amount} messages", color=0xf2da80)
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=embed)


    @commands.command(pass_context=True, aliases=['Kick', 'kIck'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title="Kicked", description=f"We have kicked the user: {member} for the reason: {reason}",
                              color=0xf2da80)
        await ctx.send(embed=embed)

    #@kick.error
    #async def kick_error(self, ctx, error):
        #if isinstance(error, commands.MissingRequiredArgument):
            #await ctx.send('Test')

    @commands.command(pass_context=True, aliases=['unBan', 'Unban'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title="Unbanned", description=f"The user {user.mention}, has been unbanned",
                                      color=0xf2da80)
                await ctx.send(embed=embed)
                return

    @commands.command(pass_context=True, aliases=['Warn', 'wArn'])
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, user: discord.User, *reason: str):
        if not reason:
            await ctx.send("```Please provide a reason```")
            return
        reason = ' '.join(reason)
        for current_user in report['users']:
            if current_user['name'] == user.id:
                current_user['reasons'].append(reason)
                break
        else:
            report['users'].append({
                'name': user.id,
                'reasons': [reason, ]

            })
        with open('reports.json', 'w+') as f:
            json.dump(report, f, indent=3)
            embed = discord.Embed(title="Warning", description=f"We have warned {user.name} of the reason {reason}",
                                  color=0xf2da80)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['Warnings', 'warnIngs'])
    async def warnings(self, ctx, user: discord.User):
        for current_user in report['users']:
            if user.id == current_user['name']:
                embed = discord.Embed(title="Warnings",
                                      description=f"{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}",
                                      color=0xf2da80)
                await ctx.send(embed=embed)
                break
        else:
            embed = discord.Embed(title="Warnings",
                                  description=f"{user.name} has not been reported according to our system",
                                  color=0xf2da80)
            await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['Ban', 'bAn'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(title="How to post a Suggestion?",
                              description="To post a suggestion, write .postsuggestion followed by your suggestion. This will then go for approval which will be looked out by our moderators.")
        await ctx.send(embed=embed)
        await ctx.send(f'Banned {member.mention}')

    @commands.command(pass_context=True, aliases=['Nickname', 'nickName', 'NickName'])
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f'```Nickname was changed for {member.mention} ```')

    @commands.command(pass_context=True, aliases=['RoleMute', 'roleMute', 'Rolemute'])
    @commands.has_permissions(manage_roles=True)
    async def rolemute(self, ctx):
        print("Test")
        guild = ctx.guild
        await guild.create_role(name="Muted")
        await ctx.send("Muted role set")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def roleadd(self, ctx, rolename=None):
        print("Test")
        guild = ctx.guild
        await guild.create_role(name=rolename)
        await ctx.send(f"Role added with the name - {rolename}")

def setup(client):
    client.add_cog(Moderation(client))
