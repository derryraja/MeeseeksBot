import aiohttp
import discord
from discord.ext import commands
import random


Token = "YOUR_BOT_TOKEN"
YOUR_PREFIX = "~"
client = commands.Bot(command_prefix=YOUR_PREFIX)


@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    # id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name,
        description=description,
        color=discord.Color.blurple()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    # embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="Ask, you shall receive", description="HAHA, meme go brr")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


@client.command(pass_context=True)
async def prequel(ctx):
    embed = discord.Embed(title="Ask, you shall receive", description="It will be done my lord")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/PrequelMemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


@client.command(pass_context=True)
async def wallpaper(ctx):
    embed = discord.Embed(title="Ask, you shall receive", description="epic")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/wallpaper/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


@client.command(pass_context=True)
async def wholesome(ctx):
    embed = discord.Embed(title="Ask, you shall receive", description="how nice")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/wholesomememes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


# @client.command(pass_context=True)
# async def YOUR_CALL_COMMAND(ctx):
#     embed = discord.Embed(title="EMBED_TITLE", description="EMBED_DESCRIPTION")
#
#     async with aiohttp.ClientSession() as cs:
#         async with cs.get('SUBREDDIT_LINK/new.json?sort=hot') as r:
#             res = await r.json()
#             embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
#             await ctx.send(embed=embed)


client.run(Token)