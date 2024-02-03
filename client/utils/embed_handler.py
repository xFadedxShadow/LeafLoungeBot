#!/usr/bin/env python3

# Imports
import nextcord

# Classes
class EmbedHandler:
    """
    Class handles all the embeds for commands, etc
    """

    def __init__(self, client):
        self.client = client

    async def welcome(self, member):
        embed = nextcord.Embed(
            title=f"Welcome {member.name}",
            description=f"Welcome to: {member.guild}",
            color=nextcord.Color.blurple()
        )
        embed.set_thumbnail("https://cdn-icons-png.flaticon.com/512/8809/8809505.png")
        embed.add_field(name="We're glad your here, Enjoy your stay!", value="", inline=False)
        embed.add_field(name="Member", value=f"__{member.mention}__", inline=False)
        embed.add_field(name="Account Creation Date", value=f"__{member.created_at.strftime('%m-%d-%Y %I:%M:%S')}__", inline=False)
        embed.set_footer(
            text=f"Client Version: {self.client.config['Client']['version']}",
            icon_url=self.client.user.avatar.url
        )

        return embed

    async def latency(self, member, latency):
        """
        Method returns an Embed for the command 'latency'
        """

        embed = nextcord.Embed(
            title="Latency Information",
            description=f"Executed by: __{member.mention}__",
            color=nextcord.Color.blurple()
        )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/5551/5551592.png")
        embed.add_field(name=f"Client Latency", value=f"__{latency}ms__", inline=False)
        embed.set_footer(
            text=f"Client Version: {self.client.config['Client']['version']}",
            icon_url=self.client.user.avatar.url
        )

        return embed

    async def userinfo(self, member, target):
        """
        Method returns an Embed for the command 'userinfo'
        """

        embed = nextcord.Embed(
            title="User Information",
            description=f"Executed by: __{member.mention}__",
            color=nextcord.Color.blurple()
        )
        embed.set_thumbnail(target.avatar.url)
        embed.add_field(name="Target User", value=f"__{target.mention}__", inline=False)
        embed.add_field(name="Username", value=f"__{target.name}__", inline=False)
        embed.add_field(name="Display Name", value=f"__{target.display_name}__", inline=False)
        embed.add_field(name="User ID", value=f"__{target.id}__", inline=False)
        embed.add_field(name="Nickname", value=f"__{target.nick}__", inline=False)
        embed.add_field(name="Join Date", value=f"__{target.joined_at.strftime('%m-%d-%Y %I:%M:%S')}__", inline=False)
        embed.add_field(name="Creation Date", value=f"__{target.created_at.strftime('%m-%d-%Y %I:%M:%S')}__", inline=False)
        embed.set_footer(
            text=f"Client Version: {self.client.config['Client']['version']}",
            icon_url=self.client.user.avatar.url
        )

        return embed

    async def dick(self, member, size, emojis):
        """
        Method returns an Embed for the 'dick' command
        """

        embed = nextcord.Embed(
            title="E-Dick Size",
            description=f"Executed by: __{member.mention}__",
            color=nextcord.Color.blurple()
        )
        embed.set_thumbnail(member.avatar.url)
        embed.add_field(name="Size", value=f"__{size} Inches__", inline=False)
        embed.add_field(name="", value=f"{emojis[0]}{emojis[1]}{emojis[2]}", inline=True)

        if size < 1.5:
            embed.add_field(name="You are a pussy...", value="", inline=True)
        elif size >= 1.5 and size < 5:
            embed.add_field(name="You need a penis pump!", value="", inline=True)
        elif size >= 5 and size < 8.5:
            embed.add_field(name="Average", value="", inline=True)
        elif size >= 8.5 and size < 12:
            embed.add_field(name="You got a big dick!", value="", inline=True)
        else:
            embed.add_field(name="Big Dick Energy!", value="", inline=True)

        embed.set_footer(
            text=f"Client Version: {self.client.config['Client']['version']}",
            icon_url=self.client.user.avatar.url
        )

        return embed

    async def rating(self, title, member, target, rating):
        embed = nextcord.Embed(
            title=f"{title} Rating",
            description=f"Executed by: __{member.mention}__",
            color=nextcord.Color.blurple()
        )
        embed.set_thumbnail(target.avatar.url)
        embed.add_field(name="Target", value=f"__{target.mention}__", inline=False)
        embed.add_field(name="Rating", value=f"__%{rating}__", inline=False)
        embed.set_footer(
            text=f"Client Version: {self.client.config['Client']['version']}",
            icon_url=self.client.user.avatar.url
        )

        return embed

    async def level_up(self, member, member_data):
        embed = nextcord.Embed(
            title="Level Up",
            description=f"__{member.mention}__ has leveled up!",
            color=nextcord.Color.blurple()
        )
        embed.set_thumbnail("https://cdn-icons-png.flaticon.com/512/6602/6602890.png")
        embed.add_field(name=f"New Level: {member_data['level']}", value="", inline=False)
        embed.set_footer(
        text=f"Client Version: {self.client.config['Client']['version']}",
        icon_url=self.client.user.avatar.url
        )

        return embed