import os

def save_data_as_csv(data, output):
    """

    :param data: Data with assigned labels using the K-Means algorithm.
    :param output: Path to the folder where the results of the K-Means algorithm will be saved.
    """
    data.to_csv(os.path.join(output,'clustered_data.csv'))
