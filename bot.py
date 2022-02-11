# Imports
from secrets import TOKEN

import hikari
import lightbulb

from database import Database as db
from extensions.economy import EconomyHelperMethods as helper_methods

# Setups for bot
bot = lightbulb.BotApp(token=TOKEN,
                       prefix=("coin ", "coin."),
                       default_enabled_guilds=(872490089731723365))

db.initialise()
bot.load_extensions("extensions.moderation")
bot.load_extensions("extensions.fun")


# Events
@bot.listen(hikari.GuildJoinEvent)
async def on_server_join(event):
    role = event.app.cache.get_roles_view_for_guild(event.guild)
    roles = role.values()

    # Create roles if not exists
    if "Muted" not in roles:
        await event.app.rest.create_role(guild=event.guild_id,
                                         name="Muted",
                                         color=0x363636,
                                         send_messages=False)


# Running the bot
bot.run()
