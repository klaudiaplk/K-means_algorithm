import argparse
import logging
import os

from K_means_algorithm.k_means_algorithm import elbow_method, k_mean_algorithm, silhouette_method
from K_means_algorithm.plots import all_clusters_plot, clusters_plots_2d
from K_means_algorithm.prepare_data import read_data, data_encoding
from K_means_algorithm.save_data import save_data_as_csv


def main():
    """Runner for this script."""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description='k_means_algorithm')
    parser.add_argument('--input-file', type=str, required=True,
                        help='The path to the csv file containing the data to be clustered.')
    parser.add_argument('--output-dir', type=str, required=True,
                        help='Path to the folder where the results of the K-Means algorithm will be saved.')
    parser.add_argument('--k-max', type=int, required=True,
                        help='Max clusters to check for Elbow or Silhouette methods')
    parser.add_argument('--n-init', type=int, required=False,
                        help='Enter the number of initializations to perform K-Means algorithm. '
                             'If nothing is entered, the default value is 10',
                        default=10)
    parser.add_argument('--max-iter', type=int, required=False,
                        help='Enter a number of maximum iterations for each initialization of the k-means algorithm. '
                             'If nothing is entered, the default value is 100',
                        default=100)
    parser.add_argument('--method', choices=['elbow', 'silhouette'], required=False,
                        help='Possibility to choose a method to determine the optimal K for K-Means Algorithm.'
                             'You can choose between \'elbow\' or \'silhouette\'. '
                             'If nothing is selected then the default will be selected \'elbow\'',
                        default='elbow')
    parser.add_argument('--plots', choices=['with', 'without'], required=False,
                        help='Possibility to choose whether you want to draw plots or '
                             'just save the results to a csv file. '
                             'If nothing is selected then the default will be selected \'with\'',
                        default='with')
    parser.set_defaults(func=start)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

def start(args):
    if not os.path.isdir(args.output_dir):
        raise Exception("The given path where to save the results does not exist! Please enter the correct one.")
    data = read_data(args.input_file)
    encoded_data = data_encoding(data)
    if args.method == 'elbow':
        elbow = elbow_method(encoded_data, args.k_max, args.output_dir)
        logging.info("The best value for elbow method proposed by kneed library is {}. "
        "You can follow it or choose the best number of groups in your opinion "
        "by looking at the chart for the elbow method. "
        "Which k for K-Means Algorithm do you choose?".format(elbow))
        k = int(input())
        while k <= 0 or k > args.k_max:
            logging.info('The number of clusters has been entered incorrectly.'
                         ' Please enter a number greater than 0 but less than '
                         'the maximum number of clusters at the beginning:')
            k = int(input())
        clustered_data, centroids = k_mean_algorithm(k, args.n_init, args.max_iter, encoded_data)
        if args.plots == 'with':
            clusters_plots_2d(clustered_data, centroids, args.output_dir, "elbow_method")
            all_clusters_plot(clustered_data, centroids, args.output_dir, "elbow_method")
    elif args.method == 'silhouette':
        silhouette_method(encoded_data, args.k_max, args.output_dir)
        logging.info("Choose the best number of groups in your opinion "
                     "by looking at the chart for the silhouette method. "
                     "Which k for K-Means Algorithm do you choose?")
        k = int(input())
        while k <= 0 or k > args.k_max:
            logging.info('The number of clusters has been entered incorrectly.'
                         ' Please enter a number greater than 0 but less than '
                         'the maximum number of clusters at the beginning:')
            k = int(input())
        clustered_data, centroids = k_mean_algorithm(k, args.n_init, args.max_iter, encoded_data)
        if args.plots == 'with':
            clusters_plots_2d(clustered_data, centroids, args.output_dir, "silhouette_method")
            all_clusters_plot(clustered_data, centroids, args.output_dir, "silhouette_method")
    save_data_as_csv(encoded_data, args.output_dir)
