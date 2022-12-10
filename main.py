import discord
import random
import Data

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

bad_words = ['avazi', 'khafe sho', 'bi tarbiat', 'bi shoor', 'oskol']
reply_choice = ['khodeti!', "bi tarbiat!", 'chendesh', 'dige tekrar nashe']

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for word in bad_words:
      if word in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention}" + " " + random.choice(reply_choice))


client.run(Data.token)

