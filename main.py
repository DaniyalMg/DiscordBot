import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run('OTAxODI3NzE2NzA0MjU2MDEw.GM6IsP.mNsx47SBzRWGz_Azq5Wgt9xSFYCevCNNTUlCC0')