import pandas as pd
from numpy import NaN


def make_condition_feature(input, cond_func, cond_name):
    temp = pd.DataFrame({cond_name: 0}, index=input.index)
    for idx in temp.index:
        temp[cond_name][idx] = cond_func(input, idx)
    return pd.concat([input.copy(), temp], axis=1)


def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def is_zavoronok(_input, idx):
    return 1 if get_sec(_input["Время пробуждения"][idx]) < get_sec("7:00:00") else 0


def early_drinking(_input, idx):
    return 1 if _input["Возраст алког"][idx] < 18 and _input["Возраст алког"][idx] != NaN  else 0