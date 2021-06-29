import discord
from discord.ext import commands

# levels: DELETE (0), KICK (1), BAN(2) 
SEVERITY = 0
BANNED_WORDS = ["fuck","shit"]

async def HandleMessage(msg):
    global SEVERITY
    if SEVERITY == 0:
        await msg.delete()
    elif SEVERITY == 1:
        msg.author.kick(reason="automod")
    elif SEVERITY == 2:
        msg.author.ban(reason="automod")
    else:
        print("[WARN]: SEVERITY isn't a valid value; defaulting to 0")
        await msg.delete
        SEVERITY = 0

class Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_message(message):
        for word in message.content.split():
            for bannedword in BANNED_WORDS:
                if word == bannedword:
                    HandleMessage(message)

    