from kneed import KneeLocator
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def elbow_method(data, k_max, output):
    """

    :param data: Date to be clustered.
    :param k_max: Max clusters to check for Elbow method.
    :param output: Path to the folder where the results of the K-Means algorithm will be saved.
    :return: Optimal k for K-Means Algorithm determined by the Elbow method.
    """
    k = np.arange(1, k_max+1)

    sse = []

    for i in k:
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)

    elbow_method_plot(k, sse, output)
    kl = KneeLocator(range(1, k_max+1), sse, curve = "convex", direction = "decreasing")
    elbow = kl.elbow
    return elbow

def elbow_method_plot(k, sse, output):
    """

    :param k: List of consecutive cluster numbers from one to k_max.
    :param sse: List of consecutive Sum of Squared Errors for the next k cluster numbers from zero to k_max.
    :param output: Path to the folder where the results of the K-Means algorithm will be saved.
    """
    plt.plot(k, sse, "o-")
    plt.xticks(k)
    plt.xlabel("K value")
    plt.ylabel("Sum of Square Errors")
    plt.title("Finding the value of K - Elbow Method")
    plt.savefig(os.path.join(output, 'Elbow_Method_results.png'))
    plt.show()
    plt.close()

def silhouette_method(data, k_max, output):
    """

    :param data: Date to be clustered.
    :param k_max: Max clusters to check for Silhouette method.
    :param output: Path to the folder where the results of the K-Means algorithm will be saved.
    """
    k = np.arange(2, k_max+1)
    silhouette_coefficients = []

    for i in k:
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(data)
        score = silhouette_score(data, kmeans.labels_)
        silhouette_coefficients.append(score)

    silhouette_method_plot(k, silhouette_coefficients, output)

def silhouette_method_plot(k, silhouette_coefficients, output):
    """

    :param k: List of consecutive cluster numbers from two to k_max.
    :param silhouette_coefficients: List of consecutive Silhouette coefficient value
     for the next k cluster numbers from zero to k_max.
    :param output: Path to the folder where the results of the K-Means algorithm will be saved.
    """
    plt.plot(k, silhouette_coefficients, "o-")
    plt.xticks(k)
    plt.xlabel("K value")
    plt.ylabel("Silhouette coefficient value")
    plt.title("Finding the value of K - Silhouette Method")
    plt.savefig(os.path.join(output, 'Silhouette_Method_results.png'))
    plt.show()
    plt.close()

def k_mean_algorithm(k, n_init, max_iter, data):
    """

    :param k: Number of clusters into which the data will be clustered.
    :param n_init: Number of initializations to perform K-Means algorithm.
    :param max_iter: Number of maximum iterations for each initialization of the k-means algorithm.
    :param data: Date to be clustered.
    :return: Data that is clustered with labels and coordinates of the centers of clusters.
    """
    kmeans = KMeans(init = "random", n_clusters = k, n_init = n_init, max_iter = max_iter, random_state = 42)
    kmeans.fit(data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    data['label'] = labels

    return data, centroids
