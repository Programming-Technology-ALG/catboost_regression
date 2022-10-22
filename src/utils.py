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



def save_as_pickle(obj, path) -> None:
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


def load_as_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


real_pipe = Pipeline([
    ('impute', SimpleImputer(strategy='constant', fill_value=0)),
    ('scaler',  StandardScaler())
])

cat_pipe = Pipeline([
    ('impute', SimpleImputer(strategy='constant', fill_value='NA')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse=False, dtype=np.int8))
])


preprocess_pipe = ColumnTransformer(transformers=[
    ('real_cols', real_pipe,    cfg.SS),
    ('cat_cols',  cat_pipe,     cfg.OHE)
])
