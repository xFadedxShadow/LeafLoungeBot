#!/usr/bin/env python3

""" Author: xFadedxShadow """

# Classes

class UserDataHandler:
    def __init__(self, client, user_data):
        self.client = client
        self.user_data = user_data

    async def check_for_user(self, user):
        """
        Method checks for a user id key in "user_data"

        Parameters:
        - user: An instance of member

        Returns:
        Method does not return anything just creates a new user in "user_data"
        """

        user_id = str(user.id)

        if user_id not in self.user_data:
            self.user_data[user_id] = {
                "level": 0,
                "xp": 0,
                "Voice": {
                    "joined_time": None,
                    "channel_id": None,
                    "voicetime": 0
                },
                "Warnings": {
                    "amount": 0,
                    "reasons": [
                        
                    ]
                }
            }
            await self.client.database.write("user_data.json", self.user_data)

    async def give_user_xp(self, user, xp):
        """
        Method give a user xp

        Parameters:
        - user: An instance of a member

        Returns:
        Method returns a boolean
        "True" if the user leveled up
        "False" if the user didn't level up
        """

        user_id = str(user.id)
        user = self.user_data[user_id]
        required_xp = user["level"] * self.client.config["LevelSystem"]["level_xp_scale"]

        user["xp"] += xp

        if user["xp"] < required_xp:
            await self.client.database.write("user_data.json", self.user_data)
            return False

        while user["xp"] >= required_xp:
            user["level"] += 1
            user["xp"] -= required_xp
            required_xp = user["level"] * self.client.config["LevelSystem"]["level_xp_scale"]

        await self.client.database.write("user_data.json", self.user_data)
        return True
