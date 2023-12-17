import discord

from .nDnDICE import nDn

client = discord.Client()


@client.event
async def on_ready():
    print("Botを起動しました。")


@client.event
async def on_message(message):
    msg = message.content
    result = nDn(msg)
    if result is not None:
        await client.send_message(message.channel, result)


# ここにbotのアクセストークンを入力
client.run("***")
