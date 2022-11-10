from discord.ext import commands
import discord
import logging
import json

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
description = ""

bot = commands.Bot(command_prefix='.', description=description, intents=intents)
handler = logging.FileHandler(filename='discord_bot.log', encoding='utf-8', mode='w')

with open('secrets.json', 'r+') as f:
    data = json.load(f)
    token = data["token"]


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('----------')


@bot.hybrid_command()
async def test(ctx):
    await ctx.send(ctx.message.author.mention + "Testing Testing 1-2-3")


@bot.hybrid_command()
async def ping(ctx):
    await ctx.send(f'{ctx.message.author.mention} is pinging me!')


@bot.hybrid_command()
async def help_me(ctx):
    await ctx.send("How can I help you?")


@bot.command()
async def sync(ctx):
    await ctx.bot.tree.sync()  # Syncs slash commands globally, may change this later.
    await ctx.send("Successfully synced all slash commands.")


@bot.hybrid_command()
async def random_wiki(ctx):
    embed = discord.Embed(
        color=discord.Colour.brand_green()
    )
    embed.add_field(name='Here is a random Wikipedia article: ',
                    value='[https://en.wikipedia.org/wiki/Special:Random]'
                          '(https://en.wikipedia.org/wiki/Special:Random)')
    await ctx.send(embed=embed)
    # await ctx.bot.tree.sync()  # Syncs slash commands globally, may change this later.


@bot.hybrid_command()
async def have_a_cookie(ctx):
    url = f"https://giphy.com/gifs/sesamestreet-xT0xeMA62E1XIlup68"
    url_two = f"https://media.giphy.com/media/xT0xeMA62E1XIlup68/giphy.gif"
    embed = discord.Embed(color=discord.Colour.random())
    embed.set_image(url=url_two)
    await ctx.channel.send(embed=embed)


@bot.hybrid_command(administrator=True)
async def shutdown(ctx):
    await ctx.send(f'This bot is being shut down by {ctx.message.author.mention}')
    await ctx.send("Shutting down...")
    await ctx.bot.close()

bot.run(token=token, log_handler=handler)
