import numpy as np
import matplotlib.pyplot as plt
import os

def clusters_plots_2d(data, centroids, output, method_name):
    """

    :param data: Data that is clustered.
    :param centroids: Coordinates of the centers of clusters.
    :param output: Path to the folder where the results of the K-Means algorithm will be saved.
    :param method_name: The name on the method of which the appropriate
    number of k was selected: elbow or silhouette.
    """
    columns_number = len(data.columns) - 1
    centers = np.array(centroids)
    for i in range(columns_number):
        for y in range(i+1, columns_number):
            current_column = data.columns[i]
            next_column = data.columns[y]
            if next_column == 'label':
                continue
            plt.scatter(data[current_column], data[next_column], c=data['label'])
            for centroid in centers:
                plt.scatter(centroid[i], centroid[y], marker="x", color='r')
            plt.title("K-Means Algorithm results")
            plt.xlabel(current_column)
            plt.ylabel(next_column)
            plt.savefig(os.path.join(output, '{}_{}_{}.png'.format(current_column, next_column, method_name)))
            plt.close()

def all_clusters_plot(data, centroids, output, method_name):
    """

    :param data: Data that is clustered.
    :param centroids: Coordinates of the centers of clusters.
    :param output: Path to the folder where the results of the K-Means algorithm will be saved.
    :param method_name: The name on the method of which the appropriate
    number of k was selected: elbow or silhouette.
    """
    columns_number = len(data.columns) - 1
    fig, axes = plt.subplots(nrows=columns_number, ncols=columns_number)
    centers = np.array(centroids)
    for i in range(columns_number):
        for y in range(columns_number):
            current_column = data.columns[i]
            next_column = data.columns[y]
            if next_column == 'label':
                continue
            axes[i, y].scatter(data[current_column], data[next_column], c=data['label'])
            for centroid in centers:
                axes[i, y].scatter(centroid[i], centroid[y], marker="x", color='r')

    # uncomment if you want to have only plots above diagonal
    # for i in range(columns_number):
    #     axes[i][i].set_visible(False)
    #     for y in reversed(range(i+1, columns_number)):
    #         axes[y][i].set_visible(False)

    cols = [col for col in data.columns]
    rows = [row for row in data.columns]

    for ax, col in zip(axes[0], cols):
        ax.set_title(col, size='small')

    for ax, row in zip(axes[:, 0], rows):
        wrapped_label = row.replace(' ', '\n')
        ax.set_ylabel(wrapped_label, rotation=90, size='small')
    fig.tight_layout()
    fig.suptitle('K-Means Algorithm results for all paired columns')
    plt.show()
    fig.savefig(os.path.join(output, 'K-Means_Algorithm_results_for_all_paired_columns_{}.png'.format(method_name)))
    plt.close()
