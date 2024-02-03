#!/usr/bin/env python3

# Imports
import os
import sys

from nextcord.ext import commands

# Classes
class OnReadyEvent(commands.Cog):
    """
    Class registers the 'on_ready' event for the client.

    Inherits 'commands.Cog'
    """

    def __init__(self, client, config):
        self.client = client
        self.config = config

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Client Event Listener: 'on_ready()'

        Returns: None
        """

        if not self.config["enabled"]:
            return

        print(f"Logged in as: '{self.client.user}' ({self.client.user.id})")

        print("\n [Loading Cogs]")

        try:
            for cog in os.listdir("commands/"):
                if not cog.endswith(".py"):
                    continue
                self.client.load_extension(f"commands.{cog[:-3]}")
                print(f"    - Cog file loaded: '{cog}' successfully!")
        except commands.ExtensionError as error:
            raise
        except OSError as error:
            sys.exit(1)

    @staticmethod
    def setup(client):
        """
        Static Method sets up the event to be registered to the client.
        """

        client.add_cog(OnReadyEvent(client, client.config["Events"]["OnReady"]))
