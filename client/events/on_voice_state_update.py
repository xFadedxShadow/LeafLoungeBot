#!/usr/bin/env python3

"""Author: xFadedxShadow"""

# Imports
import datetime

import nextcord
from nextcord.ext import commands

from utils.embed_handler import EmbedHandler
from utils.user_data_handler import UserDataHandler

# Classes
class OnVoiceStateUpdateEvent(commands.Cog):
    def __init__(self, client, config):
        self.client = client
        self.config = config

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not self.config["enabled"]:
            return

        user_data = await self.client.database.read("user_data.json")
        await UserDataHandler(self.client, user_data).check_for_user(member)
        user = user_data[str(member.id)]

        # Check for voice states changing like muting and so on.
        if not before.channel and after.channel:
            user["Voice"]["joined_time"] = datetime.datetime.now().isoformat()
            user["Voice"]["channel_id"] = member.voice.channel.id
            await self.client.database.write("user_data.json", user_data)

        elif before.channel and after.channel:
            if user["Voice"]["joined_time"] == None:
                user["Voice"]["joined_time"] = datetime.datetime.now().isoformat()

            user["Voice"]["channel_id"] = member.voice.channel.id
            await self.client.database.write("user_data.json", user_data)

        elif before.channel and not after.channel:
            if user["Voice"]["joined_time"] == None:
                return

            duration = datetime.datetime.now() - datetime.datetime.fromisoformat(user["Voice"]["joined_time"])
            total_minutes = int(round(duration.total_seconds() / 60))
            user["Voice"]["voicetime"] += total_minutes
            user["Voice"]["channel_id"] = None
            user["Voice"]["joined_time"] = None

            levels_up = await UserDataHandler(self.client, user_data).give_user_xp(member, self.config["xp"] * total_minutes)

            if levels_up:
                embed = await EmbedHandler(self.client).level_up(member, user_data[str(member.id)])
                await before.channel.send(embed=embed)

    @staticmethod
    def setup(client):
        client.add_cog(OnVoiceStateUpdateEvent(client, client.config["Events"]["OnVoiceStateUpdate"]))
