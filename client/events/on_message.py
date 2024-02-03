#!/usr/bin/env python3

# Imports
from nextcord.ext import commands

from utils.embed_handler import EmbedHandler
from utils.user_data_handler import UserDataHandler

# Classes
class OnMessageEvent(commands.Cog):
    """
    Class registers the 'on_message' event for the client.

    Inherits 'commands.Cog'
    """

    def __init__(self, client, config):
        self.client = client
        self.config = config

    @commands.Cog.listener()
    async def on_message(self, ctx):
        """
        Client Event Listener: 'on_message()'

        Returns: None
        """

        if not self.config["enabled"]:
            return

        if not ctx.guild:
            return

        if ctx.author.bot:
            return

        user_data = await self.client.database.read("user_data.json")
        await UserDataHandler(self.client, user_data).check_for_user(ctx.author)

        levels_up = await UserDataHandler(self.client, user_data).give_user_xp(ctx.author, self.config["xp"])

        if levels_up:
            embed = await EmbedHandler(self.client).level_up(ctx.author, user_data[str(ctx.author.id)])
            await ctx.channel.send(embed=embed)

    @staticmethod
    def setup(client):
        """
        Static Method sets up the event to be registered to the client.
        """

        client.add_cog(OnMessageEvent(client, client.config["Events"]["OnMessage"]))
