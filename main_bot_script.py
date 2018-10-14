# Work with Python 3.6
import discord

TOKEN = 'NTAwODA1NjUyNjg4NTM1NTY2.DqQLjA.g0H6690gVI6-ro_TttlTOxjan_o'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        print("hello")
        await client.send_message(message.channel, msg)

    if message.content.startswith('!dub') and message.channel.name.startswith('swamp'):
        print("recieved dub")
        numDubs = int(message.channel.name[message.channel.name.index('x')+1:]) + 1
        newName = message.channel.name[:message.channel.name.index('x')+1] + str(numDubs)
        print("newName = " + newName)
        try:
            await client.edit_channel(channel = message.channel, name=newName)
        except:
            print("exception")
             

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
