# IMPORTANT IMPORTS #
from asyncio.events import get_event_loop
import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button
import asyncpg
import asyncio

# UTILITARIAN IMPORTS #
from commands_economy.Account import OpenAccount, GetBankData

# CONFIGURATION IMPORTS #
from bot_token import TOKEN
from pg_password import password

async def open_account():
	user_conn = await asyncpg.connect(f'postgres://postgres:{password}@localhost:5432/users')
	await user_conn.execute('INSERT INTO users(user_id, username, discriminator, wallet, bank) VALUES($1, $2, $3, $4, $5)', 789496056043012127, 'Science Done Right', 9144, 0, 0)
	await OpenAccount(user_conn, 'Science Done Right')
	

asyncio.get_event_loop().run_until_complete(open_account())
	
# CONFIGURATION AND LINKS#
economica = commands.Bot(command_prefix = ('coin ', 'Coin ', 'coin.', 'Coin.'))
INVITE_URL = r'https://discord.com/api/oauth2/authorize?client_id=815556341766553600&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.events.stdlib.com%2Fdiscord%2Fauth%2F&scope=bot'

# COMMAND COLORS #
NORMAL = 0x006AFF
SUCCESSFUL = 0x29CC00
ERROR = 0x961515
IN_PROGRESS = 0xD6A400

# GENERAL COMMANDS #
@economica.event
async def on_ready():
	DiscordComponents(economica)
	print(f'Logged in as {economica.user.name}, no malfunctions so for.')
	print('WARNING: There is a possibility that some functions have errors. Please double check each vulnerable command before confirming the bot is fine.')

@economica.command()
async def test(ctx):
	await ctx.send(ctx.author.discriminator)

@economica.command()
async def invite(ctx):
	embed = discord.Embed(
		title = 'Invite',
		description = f'Thanks for inviting the bot! \n To invite {economica.user.name}, just click the button, choose the server and the bot wil automatically get invited!',
		color = NORMAL
		)
	embed.set_thumbnail(url = 'https://media.istockphoto.com/vectors/thank-you-vector-id1183202104?s=612x612')

	button = await ctx.send(
			embed = embed,
			components = [
				Button(style = 1, label = 'Info', custom_id = 'info'),
				Button(style = 5, label = 'Click to invite me!', url = f'{INVITE_URL}', custom_id = 'invite')
			]
		)

	interaction = await economica.wait_for('button_click')
	
	if interaction.component.custom_id == 'info':
		await interaction.respond(content = f"To invite the bot to a server, you need to have the `manage_server` permission in the server you're inviting it to. If this isn't working, report it to the support server or check your perms.")

	else:
		await ctx.send('Unfortunately, some button interaction failed. Sorry for the inconvenience!')

@economica.command()
async def credits(ctx):
	embed = discord.Embed(
		title = 'Credits',
		description = 'My forever gratitude to everyone who helped me be alive!\n My main creator is **Science Done Right#6969** (Please don\'t spam DM him!). Huge thanks to him for creating me!',
		color = NORMAL
		)

	await ctx.send(embed = embed)

# MODERATION COMMANDS #

@economica.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, * , reason = "No reason mentioned."):
	await member.kick(reason = reason)

@economica.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, * , reason = "No reason mentioned."):
	await member.ban(reason = reason)

@economica.command()
@commands.has_permissions(administrator = True)
async def warn(ctx):
	embed = discord.Embed(
		title = 'Coming soon!',
		description = 'Unfortunately the warn command is not yet implemented. Please wait until it\'s finished!',
		color = IN_PROGRESS
	)
	
	await ctx.send(embed = embed)

@economica.command()
@commands.has_permissions(administrator = True)
async def jail(ctx):
	embed = discord.Embed(
		title = 'Coming soon!',
		description = 'Unfortunately the jail command is not yet implemented. Please wait until it\'s finished!',
		color = IN_PROGRESS
	)
	
	await ctx.send(embed = embed)

@economica.command()
@commands.has_permissions(administrator = True)
async def mute(ctx):
	embed = discord.Embed(
		title = 'Coming soon!',
		description = 'Unfortunately the mute command is not yet implemented. Please wait until it\'s finished!',
		color = IN_PROGRESS
	)
	
	await ctx.send(embed = embed)

# ECONOMY COMMANDS #


# SETUP #
economica.run(TOKEN)