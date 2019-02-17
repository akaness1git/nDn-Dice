# coding: utf-8
import random
import re

text = '1d100'

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

def main():
    if judge_nDn(text):
        result,sum_dice = role_nDn(text)
        print('内訳：' + str(result))
        print('合計：' + str(sum_dice))
    else:
        print("対象外")

if __name__ == "__main__":
    main()