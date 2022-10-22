# -*- coding: utf-8 -*-
import sys
import os

from traitlets import default
sys.path.append('..')
sys.path.append(os.path.join(sys.path[0], '../../'))


import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from sklearn.model_selection import train_test_split
from src.utils import save_as_pickle, load_as_pickle
import pandas as pd
import src.config as cfg



@click.command()
@click.option('--input_data_filepath',  type=click.Path(exists=True))
@click.option('--output_selection_path', type=click.Path())
def main(input_data_filepath, output_selection_path):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('Split data into train and test')

    data = load_as_pickle(input_data_filepath)
    X_train, X_test, Y_train, Y_test = train_test_split(
                                                    data[:,:-1],
                                                    data[:,-1],
                                                    train_size=0.8,
                                                    random_state=cfg.RANDOM_STATE,
                                                    )

    save_as_pickle((X_train, X_test, Y_train, Y_test), output_selection_path)

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()