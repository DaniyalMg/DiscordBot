import discord
import random
import Data
from discord.ext import commands, tasks


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

bad_words = ['avazi', 'khafe sho', 'bi tarbiat', 'bi shoor', 'oskol']
reply_choice = ['khodeti!', "bi tarbiat!", 'chendesh', 'dige tekrar nashe']


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    set_activity.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for word in bad_words:
      if word in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention}" + " " + random.choice(reply_choice))

    await client.process_commands(message)


@client.command()
async def clear(ctx, arg):
    await ctx.channel.purge(limit=(int(arg) + 1))


@tasks.loop(seconds=10)
async def set_activity():
    guild = client.get_guild(1021834785557073980)
    mc = guild.member_count
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="" + str(mc)),status=discord.Status.do_not_disturb)


client.run(Data.token)
