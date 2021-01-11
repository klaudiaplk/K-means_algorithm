import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

def read_data(input_file):
    """

    :param input_file: The path to the csv file containing the data to be clustered.
    :return: I do not know yet.
    """
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, input_file)
    if os.path.isfile(abs_file_path):
        data = pd.read_csv(abs_file_path)
        print(data.head())
        print(data.info())
    else:
        logging.error("File does not exist! Check your path and try again!")
