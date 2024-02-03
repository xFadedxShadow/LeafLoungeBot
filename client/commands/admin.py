#!/usr/bin/env python3

# Imports
from nextcord.ext import commands

# Classes
class AdminCommands(commands.Cog):
    """
    Class registers 'admin' commands for the client.

    Inherits 'commands.Cog'
    """

    def __init__(self, client):
        self.client = client

        # Had to do this to add aliases to all the commands
        for config in self.client.config["Commands"]:
            command = getattr(self, f"{config.lower()}_command", None)

            if command:
                command.aliases = self.client.config["Commands"][config]["aliases"]

def setup(client):
    """
    Method sets up the cog to be registered to the client.
    """

    if client.config["Commands"]["enabled"]:
        client.add_cog(AdminCommands(client))
