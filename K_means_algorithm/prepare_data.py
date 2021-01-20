import logging
import os
import pandas as pd
from pandas.api.types import is_numeric_dtype

logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

def read_data(input_file):
    """

    :param input_file: The path to the csv file containing the data to be clustered.
    :return: Data in the form of data frame.
    """
    if not os.path.isfile(input_file):
        raise Exception('The path to the csv file containing the data to be clustered does not exist! '
                        'Please enter the correct one.')
    data = pd.read_csv(input_file)

    return data

def data_encoding(data):
    """

    :param data: Data in the form of data frame.
    :return: Encoded data in the form of data frame (only numerical).
    """
    nominal_columns = []

    for column in data.columns:
        if not is_numeric_dtype(data[column]):
            nominal_columns.append(column)

    encoded_data = data

    for nominal_column in nominal_columns:
        encoded_data = pd.get_dummies(encoded_data, columns=[nominal_column], prefix=[nominal_column])

    encoded_data = encoded_data.dropna()

    return encoded_data
