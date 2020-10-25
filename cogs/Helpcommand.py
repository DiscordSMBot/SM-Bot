import asyncio

import discord
from discord.ext import commands
import json
client = commands.Bot(command_prefix = ".", case_insensitive=True)
class Helpcommand(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client = commands.Bot(command_prefix=".", case_insensitive=True)




    @commands.command(pass_context = True , aliases=['Help', 'heLp', 'hElp', 'HeLp'])
    async def help(self, ctx):
        embed = discord.Embed(title="Help Categorys",
                              description="Below are the Command Categorys. To get information on specific categorys, use the commands bellow.\n **------------------------------------------------------------** \n **Help with the moderation module**```Help_Moderation ``` \n   **Help with the Miscellaneous module**```Help_Miscellaneous```   \n **Help with the Fun module** ```Help_Fun```   \n **Help with the Giveaway module**```Help_Giveaway``` \n **Help with setting up of the bot**```Help_Setup```",
                              color=0xf2da80)
        await ctx.send(embed=embed)


    @commands.command(pass_context = True , aliases=['Help_moderation', 'help_moderation', 'help_Moderation', 'help_moderatioN'])
    async def Help_Moderation(self, ctx):
        embed = discord.Embed(title="Moderation Module",
                              description="**Deletes messages from a channel** \n ```Purge | Purge (Ammount of messages)``` \n **Kicks a member from the server** ```Kick | Kick (Member) (Reason)``` \n **Ban's a user from the server** ```Ban | Ban (User) (Reason)``` \n **Unban's a user from the server** ```Unban | Unban (User)``` \n **Warn's a user which is logged** ```Warn | Warn (User) (Reason)``` \n **Shows the previous warning of the member** ```Warnings | Warnings (User)``` \n **Mutes a person for a specific amount of time** ```Mute | Mute (User ID) (Time in seconds) (Reason)``` \n **This command allows you to change yours or others nicknames** ```Nick | Nick <User> (Nickname)```  \n **This makes the mute role which is needed** ```SetMute | SetMute``` ",
                              color=0xf2da80)
        await ctx.send(embed=embed)

    @commands.command(pass_context = True , aliases=['Help_misc', 'help_misc', 'help_Misc'])
    async def Help_Misc(self, ctx):
        embed = discord.Embed(title="Miscellaneous Module",
                              description="**Searchs up information about a user** ```Userinfo | Userinfo <Member>``` \n **Checks the latency which you have** ```Ping | Ping```\n **Sets yourself to be AFK** ```Afk | Afk (Time in minutes)``` \n **Sends an invite link for the bot** ```Invite | Invite```",
                              color=0xf2da80)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['help_giveaway', 'Help_giveaway', 'help_Giveaway'])
    async def Help_Giveaway(self, ctx):
        embed = discord.Embed(title="Giveaway Module",
                              description="**Host a giveaway** ```Giveaway | Giveaway (Time in seconds) (Prize)```",
                              color=0xf2da80)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['help_fun', 'Help_fun', 'help_Fun'])
    async def Help_Fun(self, ctx):
        embed = discord.Embed(title="Fun Module",
                              description="**Asks the bot a question to answer** ```8Ball | 8ball (Question)```",
                              color=0xf2da80)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['help_setup', 'Help_setup', 'help_Setup'])
    async def Help_Setup(self, ctx):
        embed = discord.Embed(title="Setup Module",
                              description="**Setups the message log channel** ```Set Message Log | Setmlog (Channel Id)``` \n **Setup message welcome channel** ```Setwelcome | Setwelcome (Message Id)``` \n **Changes the prefix of the bot in your guild** ```Prefix | Prefix (New Prefix)```",
                              color=0xf2da80)
        await ctx.send(embed=embed)

    ##------


    @commands.command(pass_context=True)
    async def help2(self, ctx):
        embed = discord.Embed(title='SM | Help.',
                              description="**Invite Link:** https://discordapp.com/api/oauth2/authorize?client_id=456247418288209922&permissions=8&scope=bot",
                              color=0xf6d025)
        embed.add_field(name="Moderation Module",
                        value="`Warn`,`Warnings`,`Kick`,`Ban`, `Unban`, '",
                        inline=False)
        embed.add_field(name="XP Module", value="`!xpstats`", inline=False)
        embed.add_field(name="Moderation Module",
                        value="`!kick`,`!ban`,`!mute`,`!unmute`,`!clear`,`!info`,`!serverinfo`,`!privatelogging`,`!enablelogging`,`!staffvote`,`!er`,`!cr`",
                        inline=False)
        embed.add_field(name="Specific help",
                        value="You can get more specific help on each command by doing `![module]help` for example, `!funhelp` will give you a complete description of each command in that module.")

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def funhelp2(self, ctx):
        embed = discord.Embed(title="Fun Module Help.", color=0xf6d025)
        embed.add_field(name="hmmcount",
                        value="**Description:** Shows a count of how many times users have said hmm.\n**Permission Required** None\n**Arguments:** `None`\n```hmmcount```",
                        inline=False)
        embed.add_field(name="azcount",
                        value="**Description:** Shows a count of how many times users have sent a holoalphabetic message or pangram. In other words a message with every letter of the alphabet.\n**Permission Required** None\n**Arguments:** `None`\n```azcount```",
                        inline=False)
        embed.add_field(name="duck",
                        value="**Description:** Loads a random picture of a duck\n**Permission Required** None\n**Arguments:** `None`\n```!duck```",
                        inline=False)
        embed.add_field(name="dog",
                        value="**Description:** Loads a random picture of a dog\n**Permission Required** None\n**Arguments:** `None`\n```!dog```",
                        inline=False)
        embed.add_field(name="shib",
                        value="**Description:** Loads a random picture of a shiba\n**Permission Required** None\n**Arguments:** `None`\n```!shib```",
                        inline=False)
        embed.add_field(name="dab",
                        value="**Description:** Dab\n**Permission Required** None\n**Arguments:** `None`\n```!dab```",
                        inline=False)
        embed.add_field(name="channelid",
                        value="**Description:** Sends the channel id of the current channel.\n**Permission Required:** None\n**Arguments:** `None`\n```!channelid```",
                        inline=False)
        embed.add_field(name="hexcode",
                        value="**Description:** Generates a random hex color code.\n**Permission Required:** None\n**Arguments:** `None`\n```!hexcode```",
                        inline=False)
        embed.add_field(name="reverse",
                        value="**Description:** Reverses a message so that it's backwords.\n**Permission Required:** None\n**Arguments:** `Message`\n```!reverse [message]```",
                        inline=False)
        embed.add_field(name="say",
                        value="**Description:** Makes the bot repeat a message.\n**Permission Required:** None\n**Arguments:** `Message`\n```!say [message]```",
                        inline=False)
        embed.add_field(name="spam",
                        value="**Description:** Spams a user with a message. Permission is in place so that it's not overused.\n**Permission Required:** Ban Members\n**Arguments:** `User`,`Integer`,`Message`\n```!spam [@user] [int] [message]```",
                        inline=False)
        embed.add_field(name="fortune",
                        value="**Description:** Gives you a fortune cookie.\n**Permission Required:** None\n**Arguments:**`None`\n```!fortune```",
                        inline=False)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def moderationhelp2(self, ctx):
        embed = discord.Embed(title="Moderation Module Help.", color=0xf6d025)
        embed.add_field(name="privatelogging",
                        value="**Description:** Sets the channel for private logging for message edits, command uses, and deleted messages.\n**Permission Required:** Administrator\n**Arguments:** `None`\n```!privatelogging```",
                        inline=False)
        embed.add_field(name="enablelogging",
                        value="**Description:** Sets the channel for mod logging.\n**Permission Required:** Administrator\n**Arguments:** `None`\n```!enablelogging```",
                        inline=False)
        embed.add_field(name="staffvote",
                        value="**Description:** Sends an embed to vote for staff position through reacting with an upvote or downvote.\n**Permission Required:** Administrator\n**Arguments:** `member`\n```!staffvote Eric```",
                        inline=False)
        embed.add_field(name="mute",
                        value="**Description:** Mute a user.Time argument format is `<number>[s|m|h|d|w]`. An example of this is `45m` which mutes the user for 45 minutes.\n**Permission Required:** Manage Roles\n**Arguments:** `user` `time` `reason`\n```!mute @user 10h this is a reason```",
                        inline=False)
        embed.add_field(name="unmute",
                        value="**Description:** Unmute a user.\n**Permission Required:** Manage Roles\n**Arguments:** `user` `reason`\n```!unmute @user this is a reason```",
                        inline=False)
        embed.add_field(name="info",
                        value="**Description:** Gives you info on a user.\n**Permission Required:** @Moderators\n**Arguments:** `user`\n```!info @user```",
                        inline=False)
        embed.add_field(name="serverinfo",
                        value="**Description:** Gives you info on the current server.\n**Permission Required:** Administrator\n**Arguments:** `None`\n```!serverinfo```",
                        inline=False)
        embed.add_field(name="kick",
                        value="**Description:** Kicks a user from the server.\n**Permission Required:** Kick Members\n**Arguments:** `user`\n```!kick @user```",
                        inline=False)
        embed.add_field(name="ban",
                        value="**Description:** Bans a user.\n**Permission Required:** Ban Members\n**Arguments:** `user`\n```!ban @user```",
                        inline=False)
        embed.add_field(name="clear",
                        value="**Description:** Clears messages from a channel. Can only delete messages in the range of [2, 100]\n**Permission Required:** Administrator\n**Arguments:** `integer`\n```!clear 50```",
                        inline=False)
        embed.add_field(name="Create Role",
                        value="**Description:** Creates a new role and assigns a random color to it.\n**Permission Required:** Manage Roles\n**Arguments:** `Role Name`\n```!cr [role name]```",
                        inline=False)
        embed.add_field(name="Edit Role",
                        value="**Description:** Takes an existing role and assigns a random color to it.\n**Permission Required:** Manage Roles\n**Arguments:** `Role Name`\n```!er [role name]```",
                        inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Helpcommand(client))
