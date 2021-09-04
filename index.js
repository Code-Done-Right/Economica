// IMPORTS
const Discord = require('discord.js')
const client = new Discord.Client()
const config = require('./config.json')

client.once('ready', () => {
	console.log('Economica is running smoothly. WARNING: There is a very real chance there are errors in the commands. Please double check before running the bot to create minimal damage.')
})

// SETUP
client.login(config.token)