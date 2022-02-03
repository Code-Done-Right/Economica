# Imports
import hikari
import lightbulb
from secrets import TOKEN
from database import Database as db

# Setups for bot
bot = lightbulb.BotApp(
    token = TOKEN,
    prefix = ('coin ', 'coin.'),
    default_enabled_guilds = (872490089731723365)
)
db.initialise()

# Commands
@bot.command
@lightbulb.command('hello world', 'Says "Hello World!"')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond('Hello World!')

# Running the bot
bot.run()