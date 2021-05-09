import discord
from notifications import getMessage
from clicker import retriveTableData
from parsedata import saveData, parseData

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$avail'):
        await message.channel.send(getMessage())

    if message.content.startswith('$check'):
        await message.channel.send('Hold tight! I\'m checking to see what campsites are available.')
        table = retriveTableData()
        siteData = parseData(table)
        saveData(siteData)
        await message.channel.send(getMessage())

client.run('ODQwMDU2MDkxODEwMzMyNjcy.YJSpMw.v_de3IOsJvM2T4rHyaEVL21nuqE')
