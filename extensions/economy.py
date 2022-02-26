# Imports
import hikari
import lightbulb
import sys
import os

# Adds a path for importing database which requires a relative import
# Thanks to https://stackoverflow.com/questions/7505988/importing-from-a-relative-path-in-python

# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))
# from database import Database as db

economy_plugin = lightbulb.Plugin("Economy")

# Helper methods
class EconomyHelperMethods:
    async def __init__(self, db):
        self.db = db
        db.initialise()

    async def add_coins():
        pass

    async def remove_coins():
        pass

    async def register_user():
        pass

    async def get_bank_data():
        pass

    async def delete_account():
        pass

# Commands
@economy_plugin.command
@lightbulb.command('balance', 'Returns the balance of the user',aliases = ['bal'])
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def balance(ctx):
    pass

