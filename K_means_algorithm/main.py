import argparse
import logging

from K_means_algorithm.prepare_data import read_data


def main():
    """Runner for this script."""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description='k_means_algorithm')
    parser.add_argument('--input-file', type=str, required=False,
                        help='The path to the csv file containing the data to be clustered. If nothing is given, '
                             'the data will be taken from a Mall_Customer.csv file in this repository.',
                        default='../input/Mall_Customers.csv')
    # parser.add_argument('--output-file', type=str, required=False,
    #                     help='Path to save the program output with semantic analysis. If nothing is given, '
    #                          'the data will be saved in a output.txt file in this repository.',
    #                     default='output.txt')
    parser.set_defaults(func=start)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

def start(args):
    read_data(args.input_file)
