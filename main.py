import discord
from discord.ext import commands
import asyncpraw
import sys
import random
import aioconsole

darelist = ["person below me gets to choose your status","turn on the opposite theme"]
channelid = 809867341231685677
description = "glassy is horny"
reddit = asyncpraw.Reddit(client_id="GV-6UR0zc7dTeg",
                     client_secret="x8pLxsPG1-d4XHts00XglMT_IzDFzA",
                     password="M!K@10sta",
                     user_agent="backend for sus discord bot",
                     username="IndirectRent")

intents = discord.Intents.default()
intents.members = True
MostRecentPost = None

async def getURL(sub, _filter):
    rng = random.randint(0,10)
    counter = 0
    sr = await reddit.subreddit(sub)
    
    if _filter == "new": 
        async for submis in sr.new(limit=5):
            if not counter == rng:
                counter = counter + 1
            else:
                if submis.url.startswith("https://images.app.goo.gl/"):
                    rng + 1
                else:
                    return submis.url
            
    elif _filter == "hot":
       async for submis in sr.hot(limit=5):
            if not counter == rng:
                counter = counter + 1
            else:
                if submis.url.startswith("https://images.app.goo.gl/"):
                    rng + 1
                else:
                    return submis.url

    elif _filter == "contro":
        async for submis in sr.controversial(limit=5):
            if not counter == rng:
                counter = counter + 1
            else:
                if submis.url.startswith("https://images.app.goo.gl/"):
                    rng + 1
                else:
                    return submis.url
        
    elif _filter == "rising":
            if not counter == rng:
                counter = counter + 1
            else:
                if submis.url.startswith("https://images.app.goo.gl/"):
                    rng + 1
                else:
                    return submis.url
                    
    elif _filter == "top":
            if not counter == rng:
                counter = counter + 1
            else:
                if submis.url.startswith("https://images.app.goo.gl/"):
                    rng + 1
                else:
                    return submis.url
    else:
        return "incorrect filter"


bot = commands.Bot(command_prefix='$', description=description, intents=intents, help_command=None)
client = discord.Client()
changelognotsent = True



@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name='icanhasbot')
async def _bot(ctx):
    print("\nicanhasbot invoked\n>")
    await ctx.send('sus by tags, version 69')

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="porn")
async def _porn(ctx, arg0, arg1):
    print("\nsearch invoked\n>")
    if arg0 == "lesbian":
        await ctx.send(await getURL("lesbiangifs", arg1))
    elif arg0 == "hentai":
        await ctx.send(await getURL("hentai_gif", arg1))
    elif arg0 == "bella":
        await ctx.send(await getURL("kitsunehentai", arg1))
    elif arg0 == "cat" or arg0 == "pussy":
        await ctx.send(await getURL("ratemypussy", arg1))
    else:
        await ctx.send(await getURL(arg0, arg1))

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="reload")
async def _reload(ctx):
    print("\nreload invoked\n>")
    await ctx.send("Reloading...")


#The below code bans player.
@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="idban")
async def ban(ctx, id):
    await ctx.guild.ban(client.get_user(int(id)))

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="glassy")
async def _glassy(ctx):
    print("\nglassy invoked\n>")
    await ctx.send("https://media.discordapp.net/attachments/809867341231685677/811791573401468958/image0.jpg?width=565&height=754")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="ass")
async def _ass(ctx):
    print("\nass command invoked\n>")
    await ctx.send("https://media.discordapp.net/attachments/809867341231685677/811795239253573714/320x240.2.jpg")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="hornysuper")
async def _hornysuper(ctx):
    print("\nhornysuper invoked\n>")
    await ctx.send("https://media.discordapp.net/attachments/809867341231685677/812023534037237820/unknown.png?width=1200&height=677")
    
@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="howdidthishappen")
async def _howdidthishappen(ctx):
    print("\nhowdidthishappen invoked\n>")
    await ctx.send("https://cdn.discordapp.com/attachments/799388766967824422/813102015549800508/forthebot.png")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="sys")
async def sysshutdown(ctx, arg):
    print("\nsys invoked\n>")
    if (ctx.message.author.id == 704395538258460673):
        if arg == "shutdown":
            sys.exit(1)
        if arg == "invite":
            inv = await bot.get_channel(channelid).create_invite()
            await ctx.send("Permanent Invite: " + str(inv))
    else:
        await ctx.send("did you really think it would work?")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="big")
async def _big(ctx):
    print("\nbig invoked\n>")
    await ctx.send("https://cdn.discordapp.com/attachments/809867341231685677/813438950881624074/unknown.png big ass or big yosh")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="howhorny")
async def _howhorny(ctx):
    print('\nhowhorny invoked\n>')
    if ctx.message.author.id == 743898593575829514:
        await ctx.send("You're infinity% horny")
    elif ctx.message.author.id == 652022384416784392:
        await ctx.send("You're 65% horny")
    else:
        await ctx.send("You're " + str(random.randrange(100)) + "% horny")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="howhot")
async def _howhorny(ctx):
    print("\nhowhot invoked\n>")
    await ctx.send("You're " + str(random.randrange(100)) + "% hot")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="dare")
async def _dare(ctx):
    global darelist
    print("\ndare invoked\n>")
    await ctx.send(random.choice(darelist))
    
@commands.cooldown(1, 5, commands.BucketType.user)    
@bot.command(name="submitdare")
async def _submitdare(ctx, *arg0):
    print("New dare:")
    for i in arg0:
        print(i + " ", end="")
    print("",end="\n>")
    await ctx.send("check console <@!704395538258460673>")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="ph")
async def _ph(ctx):
    await ctx.send("chrisrc93@gmail.com, Lebronis#1")

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="pornhub")
async def _ph(ctx):
    await ctx.send("chrisrc93@gmail.com, Lebronis#1")

@bot.command(name="redirects")
async def _redirects(ctx):
    embed=discord.Embed(title="Redirects", description="left side is what you give the command, right side is what sub it searches it on", color=0x00ff00)
    embed.add_field(name="1:", value="lesbian -> [r/lesbiangifs](https://reddit.com/r/lesbiangift)", inline=False)
    embed.add_field(name="2:", value="hentai -> [r/hentai_gif](https://reddit.com/r/hentai_gif)", inline=False)
    embed.add_field(name="3:", value="bella -> [r/kitsunehentai](https://reddit.com/r/kitsunehentai)", inline=False)
    embed.add_field(name="4:", value="cat or pussy -> [r/ratemypussy](https://reddit.com/r/ratemypussy)", inline=False)
    await ctx.send(embed=embed)
    
@bot.event
async def on_ready():
    global changelognotsent
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="tags fail at coding"))
    
    if changelognotsent:
        embed=discord.Embed(title="Changelog", description="patches PogU", color=0x00ff00)
        embed.add_field(name="Added:", value="blacklisted //images.app.goo.gl/ everywhere cuz im dumb. nerfed cooldown to 5 seconds while only having 5 unique pron (<@!652022384416784392>)", inline=False)
        embed.add_field(name="Removed:", value="herobrine", inline=False)
        channel = bot.get_channel(842414655410012254)
        await channel.send("small boi", embed=embed)
        
    while True:
        await _input()
  
async def _input():
    global channelid
    msg = await aioconsole.ainput('>')
    if msg.startswith("set "):
        if msg.startswith("set channel "):
            print(msg[12:])
            channelid = int(msg[12:])
    elif msg.startswith("inv"):
        inv = await bot.get_channel(channelid).create_invite()
        print(inv)
    else:
        channel = bot.get_channel(channelid)
        await channel.send(msg)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="help")
async def _help(ctx):
    embedVar = discord.Embed(title="Commands", description="yay", color=0x00ff00)
    embedVar.add_field(name="$porn", value="`$porn <sub> <filter>` where sub is the type of porn you want and filter is [new/top/hot/contro/trending] for diffrent results", inline=False)
    embedVar.add_field(name="$ph or $pornhub", value="premuim pornhub acc info", inline=False)
    embedVar.add_field(name="$dare and $submitdare", value="gets a random dare, submit dares via `$submitdare <dare>`")
    embedVar.add_field(name="a list of chat triggers", value="$howhot, $howhorny, $big, $howdidthishappen, $hornysuper, $ass, $glassy and $icanhasbot")
    await ctx.channel.send(embed=embedVar)

@commands.cooldown(1, 5, commands.BucketType.user)
@bot.command(name="yesorno")
async def _yesorno(ctx, *args):
    embedVar = discord.Embed(title=" ".join(args), description="")
    message = await ctx.send(embed=embedVar)
    await message.add_reaction("👍")
    await message.add_reaction("👎")

bot.run('ODEyMzM1NzIzMTA0ODI5NTEw.YC_QmA.xtSgNKgsIn7bQdlELuYlPXFopW4')
