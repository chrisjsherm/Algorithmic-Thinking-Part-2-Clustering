"""
Clustering utility for Rice University Algorithmic Thinking Part II: Project 3.
"""
from alg_cluster import Cluster
import math


def slow_closest_pair(cluster_list):
    """
    Takes a list of Cluster objects and returns a closest pair where the pair is
    represented by a tuple (dist, idx1, idx2) with idx1 < idx2 where dist is the
    distance between the closest pair cluster_list[idx1] and cluster_list[idx2].
    This is a brute force algorithm that compares every cluster with every other
    cluster.

    @param list List of Cluster objects.

    @return tuple (dist, idx1, idx2) Dist is the distance between the closest
      pair in the cluster_list parameter cluster_list[idx1], cluster_list[idx2].
    """
    d_i_j = (float('inf'), -1, -1)
    list_len = len(cluster_list)
    for idx_i in range(list_len):
        for idx_j in range(idx_i + 1, list_len):
            dist = cluster_list[idx_i].distance(cluster_list[idx_j])
            if dist < d_i_j[0]:
                d_i_j = (dist, idx_i, idx_j)

    return d_i_j
