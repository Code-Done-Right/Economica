import discord
from discord.ext import commands

# BOT USER INFO #

coinbot = commands.Bot(command_prefix = ('coin ', 'Coin ', 'coin.', 'Coin.'))
INVITE_URL = r'https://discord.com/api/oauth2/authorize?client_id=815556341766553600&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.events.stdlib.com%2Fdiscord%2Fauth%2F&scope=bot'

# COMMAND COLORS #

NORMAL = 0x006AFF
SUCCESSFUL = 0x29CC00
ERROR = 0x961515

# GENERAL COMMANDS #
@coinbot.command()
async def invite(ctx):
	embed = discord.Embed(
		title = 'Invite',
		description = f'Thanks for inviting the bot! \n [Click me to invite the bot!]({INVITE_URL})',
		color = NORMAL
		)
	embed.set_thumbnail(url = 'https://media.istockphoto.com/vectors/thank-you-vector-id1183202104?s=612x612')

	await ctx.send(embed = embed)


# SETUP #
coinbot.run(TOKEN)