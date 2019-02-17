import discord
import random
import re

pattern = '\d{1,2}d\d{1,3}|\d{1,2}D\d{1,3}'
split_pattern = 'd|D'

# 対象の文字列かどうか
def judge_nDn(src):
    repatter = re.compile(pattern)
    result = repatter.match(src)
    if result is not None:
        return True
    return False

# 何面ダイスを何回振るか
def split_nDn(src):
    return re.split(split_pattern,src)

# ダイスを振る
def role_nDn(src):
    result = []
    sum_dice = 0
    role_index = split_nDn(src)
    role_count = int(role_index[0])
    nDice = int(role_index[1])
    
    for i in range(role_count):
        tmp = random.randint(1,nDice)
        result.append(tmp)
        sum_dice = sum_dice + tmp
    
    return result,sum_dice

client = discord.Client()

@client.event
async def on_ready():
    print('Botを起動しました。')

@client.event
async def on_message(message):
    msg = message.content
    if judge_nDn(msg):
        result,sum_dice = role_nDn(msg)
        await client.send_message(message.channel, '内訳：' + str(result))
        await client.send_message(message.channel, '合計：' + str(sum_dice))

#ここにbotのアクセストークンを入力
client.run('***')