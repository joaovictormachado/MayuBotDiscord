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


        
     
    if message.content.startswith("!d4"):
        dice = randint(1,4)
        if dice == 1:
            await message.channel.send('FALHA CRÍTICA!')
        elif dice == 4:
            await message.channel.send('ACERTO CRÍTICO!')    
        else:
            await message.channel.send("{}!".format(dice))  
 
 
    if message.content.startswith("!d6"):
        dice = randint(1,6)
        if dice == 1:
            await message.channel.send('FALHA CRÍTICA!')
        elif dice == 6:
            await message.channel.send('ACERTO CRÍTICO!')    
        else:
            await message.channel.send("{}!".format(dice))  

    if message.content.startswith("!d8"):
        dice = randint(1,8)
        if dice == 1:
            await message.channel.send('FALHA CRÍTICA!')
        elif dice == 8:
            await message.channel.send('ACERTO CRÍTICO!')    
        else:
            await message.channel.send("{}!".format(dice)) 

    if message.content.startswith("!d10"):
        dice = randint(1,10)
        if dice == 1:
            await message.channel.send('FALHA CRÍTICA!')
        elif dice == 10:
            await message.channel.send('ACERTO CRÍTICO!')    
        else:
            await message.channel.send("{}!".format(dice)) 

    if message.content.startswith("!d12"):
        dice = randint(1,12)
        if dice == 1:
            await message.channel.send('FALHA CRÍTICA!')
        elif dice == 12:
            await message.channel.send('ACERTO CRÍTICO!')    
        else:
            await message.channel.send("{}!".format(dice)) 


    if message.content.startswith("!d20"):
        dice = randint(1,20)
        if dice == 1:
            await message.channel.send('FALHA CRÍTICA!')
        elif dice == 20:
            await message.channel.send('ACERTO CRÍTICO!')    
        else:
            await message.channel.send("{}!".format(dice))                 





client.run('NjkyNTk1MDMyNTkwMzg1MTY0.Xnziug.9aK8YAEI3re6CKkyrxDU1V127KI')
