import pickle
from typing import Union
from pandas import DataFrame
from pandas.core.indexes.base import Index as PandasIndex
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import src.config as cfg
import numpy as np



def save_as_pickle(obj: Union[DataFrame, PandasIndex], path: str) -> None:
    if isinstance(obj, DataFrame):
        obj.to_pickle(path)
    elif isinstance(obj, PandasIndex):
        with open('path', 'wb') as f:
            pickle.dump(obj, f)


def save_model(model, path: str) -> None:
    pickle.dump(model, open(path, 'wb'))
    
    
def load_model(path: str):
    return pickle.load(open(path, 'rb'))


def save_encoder(encoder, path: str) -> None:
    pickle.dump(encoder, open(path, 'wb'))


def load_encoder(path: str):
    return pickle.load(open(path, 'rb'))


real_pipe = Pipeline([
    ('impute', SimpleImputer(strategy='constant', fill_value=0)),
    ('scaler',  StandardScaler())
])

cat_pipe = Pipeline([
    ('impute', SimpleImputer(strategy='constant', fill_value='NA')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse=False, dtype=np.int8))
])

preprocess_pipe = ColumnTransformer(transformers=[
    ('real_cols', real_pipe,    cfg.REAL_COLS),
    ('cat_cols',  cat_pipe,     cfg.CAT_COLS),
    ('ohe_cols', 'passthrough', cfg.OHE_COLS)
])

