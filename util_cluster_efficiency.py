"""
Utility for measuring the efficiency of clustering algorithms.
"""
from alg_cluster import Cluster
import random


def gen_random_clusters(num_clusters):
    """
    Creates a list of clusters where each cluster in the list corresponds to
    one randomly generated point in a square with corners: (+-1, +-1).

    @param int Length of the cluster list.

    @return list Clusters located at random points.
    """
    try:
        num_clusters = int(num_clusters)
    except ValueError:
        raise ValueError('num_clusters parameter must be an integer.')

    cluster_list = []
    if (num_clusters <= 0):
        return cluster_list

    for dummy_idx in range(num_clusters):
        cluster_list.append(
            Cluster(set(random.sample(range(10000, 99999), random.randint(1, 5))),
                    random.randint(-100, 100) / 100.0,
                    random.randint(-100, 100) / 100.0, random.randint(0, 1000),
                    random.random()
                    ))

    return cluster_list
