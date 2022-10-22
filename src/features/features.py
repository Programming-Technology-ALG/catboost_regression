import pandas as pd
from src.utils import load_as_pickle, save_as_pickle
import src.config as cfg


def make_condition_feature(input, cond_func, cond_name):
    temp = pd.DataFrame({cond_name: 0}, index=input.index)
    for idx in temp.index:
        temp[cond_name][idx] = cond_func(input, idx)
    return pd.concat([input.copy(), temp], axis=1)


def is_old_house(_input, idx):
    return 1 if str(_input["YearBuilt"][idx]) < "2000" else 0

def is_eternal_house(_input, idx):
    return 1 if str(_input["Foundation"][idx]) == "Stone" else 0
    

def build_all_features(df):
    df = make_condition_feature(df, is_old_house, cfg.IS_OLD_HOUSE)
    df = make_condition_feature(df, is_eternal_house, cfg.IS_ETERNAL_HOUSE)
    return df