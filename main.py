import discord
from discord.enums import NotificationLevel
from discord.ext import commands

from cogs.filter import Filter

client = discord.Client()
bot = commands.Bot(command_prefix="$", help_command=None, description="Basic discord.py bot")

false = False
true = True

@bot.event
async def on_ready():
    print("Loading cogs...")
    print("Starting filter...", end=None)
    bot.add_cog(Filter(bot))
    print("done")
    print("Started!")

@bot.command(name="help")
async def _help(ctx):
    embed = discord.Embed(title="Help", footer="[GitHub](https://github.com/zTags/BasicDiscordBot)")
    embed.add_field(name="Arguments", value="<arg> is required, [arg] is optinal, run `$<command>` help for detailed help", inline=false)
    embed.add_field(name="Moderation Commands", value="```$nickname <user> [nickname], ```", inline=false)
    await ctx.send(embed=embed)

    
def init():
    token = input("Your bot token:")
    bot.run(token)

init()