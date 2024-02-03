#!/usr/bin/env python3

# Imports
import random

import nextcord
from nextcord.ext import commands

from utils.embed_handler import EmbedHandler

# Classes
class MemberCommands(commands.Cog):
    """
    Class registers 'member' commands for the client.

    Inherits 'commands.Cog'
    """

    def __init__(self, client):
        self.client = client

        # Had to do this to add aliases to all the commands
        for config in self.client.config["Commands"]:
            command = getattr(self, f"{config.lower()}_command", None)

            if command:
                command.aliases = self.client.config["Commands"][config]["aliases"]

    @commands.command(name="latency", description="Grabs the clients latency information.")
    async def latency_command(self, ctx):
        config = self.client.config["Commands"]["Latency"]

        if not config["enabled"]:
            return

        if not ctx.guild:
            return

        if ctx.author.bot:
            return await ctx.send("Bots cannot run commands.")

        latency = round(self.client.latency * 1000, 2)
        embed = await EmbedHandler(self.client).latency(ctx.author, latency)

        return await ctx.reply(embed=embed)

    @commands.command(name="userinfo", description="Grabs the target users information.")
    async def userinfo_command(self, ctx, target: nextcord.Member):
        config = self.client.config["Commands"]["UserInfo"]

        if not config["enabled"]:
            return

        if not ctx.guild:
            return

        if ctx.author.bot:
            return await ctx.send("Bots cannot run commands.")

        if target.bot:
            return await ctx.send("Target cannot be a bot.")

        embed = await EmbedHandler(self.client).userinfo(ctx.author, target)

        return await ctx.reply(embed=embed)

    @commands.command(name="dick", description="Gives the member a random dick size.")
    @commands.cooldown(1, 2700, commands.BucketType.user)
    async def dick_command(self, ctx):
        config = self.client.config["Commands"]["Dick"]

        if not config["enabled"]:
            return

        if not ctx.guild:
            return

        if ctx.author.bot:
            return await ctx.send("Bots cannot run commands.")

        size = round(random.uniform(0.0, 13.0), 2)
        pp1 = nextcord.utils.get(ctx.guild.emojis, name="pp1")
        pp2 = nextcord.utils.get(ctx.guild.emojis, name="pp2")
        pp3 = nextcord.utils.get(ctx.guild.emojis, name="pp3")
        pp2 = "".join(str(pp2) for _ in range(round(size)))

        embed = await EmbedHandler(self.client).dick(ctx.author, size, [pp1, pp2, pp3])

        return await ctx.reply(embed=embed)

    @commands.command(name="fake", description="Gives the user a 'Fake' rating.")
    async def fake_command(self, ctx, target: nextcord.Member):
        config = self.client.config["Commands"]["Fake"]

        if not config["enabled"]:
            return

        if not ctx.guild:
            return

        if ctx.author.bot:
            return await ctx.send("Bots cannot run commands.")

        rating = round(random.uniform(0.0, 100.0), 2)

        embed = await EmbedHandler(self.client).rating("Fake", ctx.author, target, rating)

        return await ctx.reply(embed=embed)

    @commands.command(name="simp", description="Gives the user a 'Simp' rating.")
    async def simp_command(self, ctx, target: nextcord.Member):
        config = self.client.config["Commands"]["Simp"]

        if not config["enabled"]:
            return

        if not ctx.guild:
            return

        if ctx.author.bot:
            return await ctx.send("Bots cannot run commands.")

        rating = round(random.uniform(0.0, 100.0), 2)

        embed = await EmbedHandler(self.client).rating("Simp", ctx.author, target, rating)

        return await ctx.reply(embed=embed)

    @commands.command(name="gay", description="Gives the user a 'Gay' rating.")
    async def gay_command(self, ctx, target: nextcord.Member):
        config = self.client.config["Commands"]["Gay"]

        if not config["enabled"]:
            return

        if not ctx.guild:
            return

        if ctx.author.bot:
            return await ctx.send("Bots cannot run commands.")

        rating = round(random.uniform(0.0, 100.0), 2)

        embed = await EmbedHandler(self.client).rating("Gay", ctx.author, target, rating)

        return await ctx.reply(embed=embed)


def setup(client):
    """
    Method sets up the cog to be registered to the client.
    """

    if client.config["Commands"]["enabled"]:
        client.add_cog(MemberCommands(client))
