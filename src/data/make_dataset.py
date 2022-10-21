# -*- coding: utf-8 -*-
import sys
import os
sys.path.append('..')
sys.path.append(os.path.join(sys.path[0], '../../'))

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from src.utils import save_as_pickle
from src.data.preprocess import preprocess_data, preprocess_target, extract_target
import pandas as pd


@click.command()
@click.option('--input_filepath',           type=click.Path(exists=True))
@click.option('--output_data_filepath',     type=click.Path())
@click.option('--output_target_filepath',   type=click.Path())
@click.option('--input_target_filepath', default=".", type=click.Path(exists=True))

def main(input_filepath, output_data_filepath, input_target_filepath=".", output_target_filepath=None):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    if input_target_filepath != ".":
        df_data = pd.read_csv(input_filepath)
        df_data = preprocess_data(df_data)
        save_as_pickle(df_data, output_data_filepath)
        if output_target_filepath:
            df_target = pd.read_csv(input_target_filepath)
            df_target = preprocess_target(df_target)
            save_as_pickle(df_target, output_target_filepath)
    else:
        df = pd.read_csv(input_filepath)
        df = preprocess_data(df)
        df, target = extract_target(df)
        save_as_pickle(df, output_data_filepath)
        if output_target_filepath:
            target = preprocess_target(target)
            save_as_pickle(target, output_target_filepath)
    
    logger.info(f'Target saved to {output_target_filepath}')
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