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
from src.utils import save_as_pickle, load_as_pickle
from src.data.preprocess import preprocess_data
import pandas as pd


@click.command()
@click.option('--input_filepath',     default="../data/raw/train.csv",       type=click.Path(exists=True))
@click.option('--output_data_filepath', default="../data/processed/train_data.pkl",    type=click.Path())
@click.option('--output_encoder_filepath', default="../data/processed/preprocess_data_pipe.pkl",   type=click.Path())
@click.option('--output_target_filepath', default="../data/processed/train_target.pkl",   type=click.Path())
@click.option('--is_val', default=False, type=bool)

def main(input_filepath, output_data_filepath, output_target_filepath,  output_encoder_filepath, is_val):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    df = pd.read_csv(input_filepath)

    df = preprocess_data(df, output_encoder_filepath, is_val)
    save_as_pickle(df, output_data_filepath)
    df = load_as_pickle(output_data_filepath)

    save_as_pickle(df, output_target_filepath)
    df = load_as_pickle(output_target_filepath)
    logger.info(f'Dataset saved to {output_data_filepath}')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()