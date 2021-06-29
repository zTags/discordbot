import discord
from discord.ext import commands

class Moderation(commands.cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command
    async def ban(ctx, *arg):
        if not arg[0].startswith("<@!"):
            embed=discord.Embed(title="Error", description="in mention parsing", color=0x00ff00, footer="[GitHub](https://github.com/zTags/discordbot)")
            embed.add_field(name="Mention didnt start with <@!, did you put the mention at the beginning?", value=None, inline=False)
            await ctx.send(embed=embed)
        else:
            id = arg[1][3:arg[0].length-1]
            user = ctx.guild.get_member(int(id))
            if not user == None:
                user.ban(reason="automod")
            else:
                embed=discord.Embed(title="Error", description="user was None", color=0x00ff00, footer="[GitHub](https://github.com/zTags/discordbot)")
                embed.add_field(name="Something went wrong, was the user in the server?", value=None, inline=False)
                await ctx.send(embed=embed)
