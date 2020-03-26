import discord
import asyncio
from random import randint

client = discord.Client()

@client.event
async def on_ready():
    print('Precisa de algo mestre?')

@client.event
async def on_message(message):
    if message.author == client.user:
        return None
    print(message.content)

    if message.content.startswith("!test"):
        await message.channel.send("Sim mestre!")

    if message.content.startswith("!d3"):
        dice = randint(1,3)
        if dice == 1:
            await message.channel.send('Você se fodeu!')
        else:
            await message.channel.send("{}!".format(dice))  

client.run('#token do bot)
