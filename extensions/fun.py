import hikari
import lightbulb

fun_plugin = lightbulb.Plugin("Fun Commands")


@fun_plugin.command
@lightbulb.command("hello", 'Says "Hello World!"')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond("Hello World!")


# Loading
def load(bot):
    bot.add_plugin(fun_plugin)


def unload(bot):
    bot.remove_plugin(fun_plugin)
