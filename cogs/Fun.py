import asyncio

import discord
from discord.ext import commands, tasks
import json
import os
import datetime
from discord.utils import get
import random
from random import randint

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['8ball', '8Ball'])
    async def _8ball(ctx, *, question):
        responses = ['Yes!', 'No!', 'Honestly you tried but you will never succeed',
                     'I do not know what to say about that', 'Honestly, Yes!',
                     'Do cows know how to use the internet? No', 'Do you know how to type? Yes']
        await ctx.send({random.choice(responses)})



def setup(client):
    client.add_cog(Fun(client))