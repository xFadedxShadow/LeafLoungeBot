#!/usr/bin/env python3

# Imports
import os
import json
import atexit
import shutil
import asyncio

import nextcord
from nextcord.ext import commands

from events.on_ready import OnReadyEvent
from events.on_message import OnMessageEvent
from events.on_member_join import OnMemberJoinEvent
from events.on_command_error import OnCommandErrorEvent
from events.on_voice_state_update import OnVoiceStateUpdateEvent

from utils.database_handler import Database

# Variables
intents = nextcord.Intents.all()
intents.messages = True
client = commands.Bot(intents=intents)
client.database = Database("databases/")

# Methods
def get_config():
    """
    This method returns the clients configuration.
    Configuration path: 'client/config.cfg'

    Returns: 'json.loads()'
    """

    try:
        with open("config.cfg") as config:
            return json.loads(config.read())
    except (OSError, json.JSONDecodeError) as error:
        raise

def get_token():
    """
    This method returns the clients token.
    Token path: 'client/TOKEN'

    Returns: String
    """

    try:
        with open("TOKEN", "r") as TOKEN:
            return TOKEN.read()
    except OSError as error:
        raise

def create_databases():
    """
    This method creates json databases if they don't already exist.

    Returns: None
    """

    for database in client.config["Databases"]:
        if os.path.exists(f"databases/{database}"):
            continue
        asyncio.run(client.database.create_database(database))

def cleanup():
    """
    This method cleans up any data for the client.

    Returns: None
    """

    print("\nCleaning up..")

    try:
        for root, dirs, files in os.walk(os.path.dirname(os.getcwd())):
            if "__pycache__" not in dirs:
                continue
            shutil.rmtree(os.path.join(root, "__pycache__"))
    except OSError as error:
        raise

    user_data = asyncio.run(client.database.read("user_data.json"))

    for user in user_data:
        user = user_data[user]
        user["Voice"]["channel_id"] = None
        user["Voice"]["joined_time"] = None

    asyncio.run(client.database.write("user_data.json", user_data))

# Initialization
if __name__ == "__main__":
    atexit.register(cleanup)

    client.config = get_config()
    client.command_prefix = client.config["Client"]["prefix"]

    create_databases()

    if client.config["Events"]["enabled"]:
        OnReadyEvent.setup(client)
        OnMessageEvent.setup(client)
        OnMemberJoinEvent.setup(client)
        OnCommandErrorEvent.setup(client)
        OnVoiceStateUpdateEvent.setup(client)

    client.run(get_token())
