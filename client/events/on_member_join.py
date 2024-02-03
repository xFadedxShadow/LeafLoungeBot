#!/usr/bin/env python3

"""Author: xFadedxShadow"""

# Imports
import nextcord
from nextcord.ext import commands

from utils.embed_handler import EmbedHandler

# Classes
class OnMemberJoinEvent(commands.Cog):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if not self.config["enabled"]:
            return

        if member.bot:
            return

        welcome_channel = member.guild.get_channel(self.config["channel_id"])
        embed = await EmbedHandler(self.client).welcome(member)

        await welcome_channel.send(embed=embed)

        if len(self.config["autoroles"]) < 1:
            return

        for role_id in self.config["autoroles"]:
            role = member.guild.get_role(role_id)
            await member.add_roles(role)

    @staticmethod
    def setup(client):
        client.add_cog(OnMemberJoinEvent(client, client.config["Events"]["OnMemberJoin"]))