#!/usr/bin/env python3

"""Author: xFadedxShadow"""

# Imports
import os
import json
import shutil
import datetime

# Classes
class Database:
    def __init__(self, database_folder):
        self.database_folder = database_folder
        self.default_data = "{}"

    async def create_database(self, database_name):
        """
        Method creates a non existing database

        Parameters:
        - database_name: a file name for the new database

        Returns: A string if the database already exist.
        """

        if not database_name.endswith('.json'):
            database_name += ".json"

        database_path = os.path.join(self.database_folder, database_name)

        if os.path.exists(database_path):
            return "Database already exists."

        try:
            with open(database_path, 'w', encoding='utf-8') as file:
                file.write(self.default_data)
        except OSError as e:
            print(f'{type(e)}: {e}')
            raise

    async def backup_database(self, database):
        """
        Method backups a database

        Parameters:
        - database: the file name for the database

        Returns: A string if the database doesn't exist.
        """

        if not database.endswith('.json'):
            database += ".json"

        database_path = os.path.join(self.database_folder, database)

        if not os.path.exists(database_path):
            return "Database doesn't exist."

        date = datetime.datetime.now().strftime('_%m-%d-%Y_%I:%M:%S')

        try:
            shutil.copy2(database_path, os.path.join(self.database_folder, 'backups', database + date + '.bk'))
        except OSError as e:
            print(f'{type(e)}: {e}')
            raise

    async def read(self, database):
        """
        Method reads json data from a database

        Parameters:
        - database: the file name for the database

        Returns: A python object
        """

        if not database.endswith('.json'):
            database += ".json"

        database_path = os.path.join(self.database_folder, database)

        if not os.path.exists(database_path):
            return "Database doesn't exist."

        try:
            with open(database_path, 'r', encoding='utf-8') as file:
                return json.loads(file.read())
        except (OSError, json.JSONDecodeError) as e:
            print(f'{type(e)}: {e}')
            raise

    async def write(self, database, data, indent=2):
        """
        Method writes data to a database

        Parameters:
        - database: the file name for the database
        - data: json data to write to database
        - indent: indentation of json data

        Returns: A string if the database doesn't exist.
        """

        if not database.endswith('.json'):
            database += '.json'

        database_path = os.path.join(self.database_folder, database)

        if not os.path.exists(database_path):
            return "Database doesn't exist."

        try:
            with open(database_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=indent)
        except (OSError, json.JSONDecodeError) as e:
            print(f'{type(e)}: {e}')
            raise
