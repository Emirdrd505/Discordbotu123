import discord

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$cam_sise'):
        await message.channel.send("Cam siseler ile işiniz bitince cam geri donusum kutusuna atmalisiniz")
    elif message.content.startswith('$kagit'):
        await message.channel.send("kagitleri kullandiktan sonra kagit geri donuşum kutusuna atmalisin")
    elif message.content.startswith('$konserve_kutusu'):
        await message.channel.send("konserve kutularını saksı olarak geri dönüştürebiliriz")
    
    else:
        await message.channel.send(message.content)


client.run("")
