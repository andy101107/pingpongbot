import discord
token = 'ODkxNTQ0OTUyMDUwNDI5OTUy.YU_58A.nWYJHmErKZ5Z3O0nsPH-rL4IfOA'
client = discord.Client()

@client.event
async def on_message(message):
    if message.content == "/핑":
        await message.channel.send("pong")
client.run(token)