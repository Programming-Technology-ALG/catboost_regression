from ctypes.wintypes import tagRECT
import pandas as pd
import numpy as np
import src.config as cfg
from src.utils import preprocess_pipe, save_as_pickle, load_as_pickle
from src.features.features import build_all_features


def cast_types(df: pd.DataFrame) -> pd.DataFrame:
    df[cfg.SS] = df[cfg.SS].astype(np.float32)
    return df

def extract_target(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(cfg.TARGET_COLS, axis=1), df[cfg.TARGET_COLS]


def preprocess_data(df, output_encoder_filepath, is_val):
    df =  df.set_index(cfg.ID_COL)
    df = cast_types(df)
    df = build_all_features(df)
    if is_val:
        Transformer = load_as_pickle(output_encoder_filepath)
        df = Transformer.transform(df)
        return df
    else:
        df, target = extract_target(df)
        Transformer = preprocess_pipe.fit(df)
        save_as_pickle(Transformer, output_encoder_filepath)
        Transformer = load_as_pickle(output_encoder_filepath)
        df = Transformer.transform(df)
        return np.concatenate([df, target], axis=1)