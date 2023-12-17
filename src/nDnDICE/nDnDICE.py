# coding: utf-8
import random
import re
import time
from typing import Any, Optional

pattern = r"\d{1,2}d\d{1,3}|\d{1,2}D\d{1,3}"
split_pattern = "d|D"
random.seed(time.time())


# 対象の文字列かどうか
def judge_nDn(src: str) -> bool:
    """
    対象の文字列かどうか

    Parameters
    ----------
    src : str
        入力文字列

    Returns
    -------
    bool
        判定
    """
    re_patter = re.compile(pattern)
    result = re_patter.fullmatch(src)
    if result is not None:
        return True
    elif src == "1d114514" or src == "1D114514":
        return True
    return False


# 何面ダイスを何回振るか
def split_nDn(src: str) -> list[str | Any]:
    """
    何面ダイスを何回振るか

    Parameters
    ----------
    src : str
        入力文字

    Returns
    -------
    list[str | Any]
        ロール回数
    """
    return re.split(split_pattern, src)


# ダイスを振る
def role_nDn(src: str) -> tuple[list[int], int, bool]:
    """
    ダイスを振る

    Parameters
    ----------
    src : str
        入力文字

    Returns
    -------
    tuple[list, int, bool]
        出目の結果,出目の合計,1ダイスか否か
    """
    result = []
    sum_dice = 0
    role_index = split_nDn(src)
    role_count = int(role_index[0])
    nDice = int(role_index[1])

    for _ in range(role_count):
        tmp = random.randint(1, nDice)
        result.append(tmp)
        sum_dice = sum_dice + tmp

    is1dice = True if role_count == 1 else False

    return result, sum_dice, is1dice


def nDn(text: str) -> Optional[str]:
    if judge_nDn(text):
        result, sum_dice, is1dice = role_nDn(text)
        if is1dice:
            return "ダイス：" + text + "\n出目：" + str(sum_dice)
        else:
            return "ダイス：" + text + "\n出目：" + str(result) + "\n合計：" + str(sum_dice)
    else:
        return None
