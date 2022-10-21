import pandas as pd
import numpy as np
import src.config as cfg
from src.utils import preprocess_pipe, save_encoder, load_encoder

def cast_types(df: pd.DataFrame) -> pd.DataFrame:
    ohe_int_cols = df[cfg.OHE].select_dtypes('number').columns
    df[ohe_int_cols] = df[ohe_int_cols].astype(np.int8)
    df[cfg.SS] = df[cfg.SS].astype(np.float32)
    return df


def preprocess_data(df: pd.DataFrame, output_encoder_filepath, is_val) -> pd.DataFrame:
    df =  df.set_index(cfg.ID_COL)
    df = cast_types(df)
    if is_val:
        df = pd.concat([df, 0])
        transformer = load_encoder(output_encoder_filepath)
        df = transformer.transform(df)
    else:
        preprocess_pipe.fit(df)
        save_encoder(preprocess_pipe, output_encoder_filepath)
        df = preprocess_pipe.transform(df)
    return df