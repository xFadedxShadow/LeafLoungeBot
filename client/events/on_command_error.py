#!/usr/bin/env python3

# Imports
from nextcord.ext import commands

# Classes
class OnCommandErrorEvent(commands.Cog):
    """
    Class registers the 'on_command_error' event for the client.

    Inherits 'commands.Cog'
    """

    def __init__(self, client, config):
        self.client = client
        self.config = config

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        Client Event Listener: 'on_command_error()'

        Returns: Message to channel where member executed command.
        """

        if not self.config["enabled"]:
            return

        if isinstance(error, commands.CommandNotFound):
            return

        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send("Missing required argument. Please check the command usage.")

        if isinstance(error, commands.BadArgument):
            return await ctx.send("Invalid argument provided. Please check the command usage.")

        if isinstance(error, commands.CommandOnCooldown):
            hours = round(int(error.retry_after)) // 3600
            minutes = round(int(error.retry_after % 3600)) // 60
            seconds = round(error.retry_after % 60)
            return await ctx.send(f"This command is on cooldown. \nPlease try again in {hours} hours {minutes} minutes {seconds} seconds.")

        if isinstance(error, commands.MissingPermissions):
            return await ctx.send("You don't have the required permissions to run this command.")

        if isinstance(error, commands.BotMissingPermissions):
            return await ctx.send("The bot doesn't have the required permissions to execute this command.")


    @staticmethod
    def setup(client):
        """
        Static Method sets up the event to be registered to the client.
        """

        client.add_cog(OnCommandErrorEvent(client, client.config["Events"]["OnCommandError"]))
