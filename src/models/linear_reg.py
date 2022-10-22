# -*- coding: utf-8 -*-
import sys
import os
sys.path.append('..')
sys.path.append(os.path.join(sys.path[0], '../../'))

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from src.utils import save_as_pickle, load_as_pickle
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression



@click.command()
@click.option('--input_data_filepath', type=click.Path(exists=True))
@click.option('--output_model_filepath', type=click.Path())
@click.option('--output_metrics_filepath')

def main(input_data_filepath, output_model_filepath, output_metrics_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


    X_train, X_test, Y_train, Y_test = load_as_pickle(input_data_filepath)

    model = LinearRegression()
    model.fit(X_train, Y_train)
    save_as_pickle(model, output_model_filepath)

    with open(output_metrics_filepath, 'w') as f:
        f.write('MAE on train: {}\n'.format(mean_absolute_error(Y_train, model.predict(X_train))))
        f.write('MAE on test: {}\n'.format(mean_absolute_error(Y_test, model.predict(X_test))))

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()