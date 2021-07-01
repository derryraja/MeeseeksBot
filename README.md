# MeeseeksBot

Meeseeks, is a Discord Bot that shares posts, memes and gifs straight from Reddit to your discord server. 
Create a new application at [Discord Developer Portal](https://discord.com/developers/applications), and then select 'Add Bot' to receive your token.

### Installation

```
Token = "YOUR_BOT_TOKEN"
YOUR_PREFIX = "~"
client = commands.Bot(command_prefix=YOUR_PREFIX)
```

- `YOUR_TOKEN`, the token of the bot available on the [Discord Developers](https://discord.com/developers/applications) section once you created the bot. Simply copy and paste it here.
- `YOUR_PREFIX = "~"`, the prefix that will be set to use the bot and access commands. (e.g "!", "$", ".", "~")

Install all the dependencies and Run the Meeseeks.py to turn on the bot!

### Predefined Commands

- `YOUR_PREFIX`meme, shares memes from r/dankmemes.
- `YOUR_PREFIX`prequel, shares starwars memes from r/prequelmemes. 
- `YOUR_PREFIX`wallpaper, shares wallpapers from r/wallpaper.
- `YOUR_PREFIX`wholesome, shares memes from r/wholesomememes.

### Add your favorite subreddits

```
@client.command(pass_context=True)
async def YOUR_CALL_COMMAND(ctx):     //Change this: YOUR_CALL_COMMAND = How you want to reference that subreddit post.
    embed = discord.Embed(title="EMBED_TITLE", description="EMBED_DESCRIPTION")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('SUBREDDIT_LINK/new.json?sort=hot') as r: //Change this: Insert the subreddit link here.
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
```

Hope you like it! ❤️
