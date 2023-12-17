import os

import discord

from .nDnDICE import nDn

client = discord.Client()


@client.event
async def on_ready() -> None:
    print("Botを起動しました。")


@client.event
async def on_message(message: discord.Message) -> None:
    msg = message.content
    result = nDn(msg)
    if result is not None:
        await client.send_message(message.channel, result)


# discord botのトークンは環境変数DICE_BOT_TOKENに保存
def bot_run() -> None:
    client.run(os.getenv("DICE_BOT_TOKEN"))
