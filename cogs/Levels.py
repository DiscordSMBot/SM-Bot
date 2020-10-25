import discord
from discord.ext import commands

import json
import asyncio


class Levels(commands.Cog):
    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(Levels(client))
