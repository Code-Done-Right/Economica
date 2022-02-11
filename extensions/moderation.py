# Imports
import os
import sys
import time

import hikari
import lightbulb

moderation_plugin = lightbulb.Plugin("Moderation")


# Time converter
def time_converter(time):
    """
    helper method `time_converter`

    Converts the given time in seconds. Ex:
    30m -> 30 minutes -> 1800s
    7d -> 7 days -> 604,800s
    """


@moderation_plugin.command
@lightbulb.option("reason", "Reason for muting the user.", type=str)
@lightbulb.option("time", "Time duration of the mute.")
@lightbulb.option("user", "User to be muted.", type=hikari.Member)
@lightbulb.command("mute", "Mutess a user for a specified time interval.")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def mute(ctx):
    await ctx.respond(
        f"{ctx.options.user} has been muted for {ctx.options.time}.")
    await ctx.respond(f"Reason: {ctx.options.reason}.")


@moderation_plugin.command
@lightbulb.option("reason", "Reason for kicking the user.", type=str)
@lightbulb.option("user", "User to be kicked.", type=hikari.Member)
@lightbulb.command("kick", "Kicks a user from the guild.")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def kick(ctx):
    await ctx.options.user.kick(reason=ctx.options.reason)
    await ctx.respond(f"{ctx.options.user} has been kicked from the server.")
    await ctx.respond(f"Reason: {ctx.options.reason}")


@moderation_plugin.command
@lightbulb.option("reason", "Reason for banning the user.", type=str)
@lightbulb.option("days_delete",
                  "deletes the messages specified by this property.",
                  type=int)
@lightbulb.option("user", "User to be banned.", type=hikari.Member)
@lightbulb.command("ban", "Bans a user from the guild.")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def ban(ctx):
    await ctx.options.user.ban(delete_message_days=ctx.options.days_delete,
                               reason=ctx.options.reason)


@moderation_plugin.command
@lightbulb.option("reason", "Reason for unbanning the user.", type=str)
@lightbulb.option("user", "User to be unbanned.", type=hikari.Member)
@lightbulb.command("unban", "Unbans a user from the guild.")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def unban(ctx):
    await ctx.options.user.unban(reason=ctx.options.reason)


# Loading the plugin
def load(bot):
    bot.add_plugin(moderation_plugin)


def unload(bot):
    bot.remove_plugin(moderation_plugin)
