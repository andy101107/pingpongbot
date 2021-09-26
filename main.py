import discord
import os
client = discord.Client()

@client.event
async def on_message(message):
    if message.content == "/핑":
        await message.channel.send("pong")
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
