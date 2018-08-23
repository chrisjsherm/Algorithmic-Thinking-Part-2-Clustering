"""
Clustering utility for Rice University Algorithmic Thinking Part II: Project 3.
"""
from alg_cluster import Cluster


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


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Takes a list of Cluster objects and two floats, horiz_center and half_width.
    Returns a tuple corresponding to the closest pair of clusters that lie in 
    the specified strip (the pair of indices should be in ascending order).

    @param list List of Cluster objects.
    @param float Horizontal position of the center line for a vertical strip.
    @param float Maximal distance of any point in the strip from the center line.

    @return tuple (dist, idx1, idx2) Dist is the distance between the closest
      pair of clusters in the specified strip.
    """
    # Build an array, strip, that contains points closer than half_width to,
    # horiz_center, the line passing through the middle point.
    strip = []
    for idx_i in range(len(cluster_list)):
        if(abs(cluster_list[idx_i].horiz_center() - horiz_center) < half_width):
            strip.append(cluster_list[idx_i])

    # Initialize the minimum distance.
    min_distance = half_width

    # Sort strip by y-coordinates.


def fast_closest_pair(cluster_list):
    """
    Takes a list of Cluster objects and returns a closest pair where the pair is
    represented by a tuple (dist, idx1, idx2) with idx1 < idx2 where dist is the
    distance between the closest pair cluster_list[idx1] and cluster_list[idx2].
    This is a divide and conquer algorithm.

    @param list List of Cluster objects.

    @return tuple (dist, idx1, idx2) Dist is the distance between the closest
      pair in the cluster_list parameter cluster_list[idx1], cluster_list[idx2].
    """
    pass

def merge_sort(arr, left, right):
    """
    Divide and conquer algorithm for sorting elements in a stable fashion.

    @param array Elements to sort.
    @param int First index of the left half of the array.
    @param int Last index of the right half of the array.
    """
    if left < right:
        middle = (left + right) // 2

        # Sort first and second halves.
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        merge(arr, left, middle, right)

def merge(arr, left, middle, right):
    """
    Merge the two subarrays of arr. 
    The first subarray is arr[left:middle].
    The second subarray is arr[middle+1:right]

    @param array Elements of the subarrays.
    @param int First index of the left subarray.
    @param int Middle index of the array.
    @param int Last index of the right subarray.
    """
    len_left_arr = middle - left + 1
    len_right_arr = right - middle

    temp_left = [0] * len_left_arr
    temp_right = [0] * len_right_arr

    # Copy data into temporary arrays.
    for idx_i in range(0, len_left_arr):
        temp_left[idx_i] = arr[left + idx_i]
    for idx_i in range(0, len_right_arr):
        temp_right[idx_i] = arr[middle + 1 + idx_i]

    idx_i = 0  # Initial index of the left subarray.
    idx_j = 0  # Initial index of the right subarray.
    idx_k = left  # Initial index of merged subarray.

    # Merge the sorted temp arrays back into arr.
    while idx_i < len_left_arr and idx_j < len_right_arr:
        if temp_left[idx_i] <= temp_right[idx_j]:
            arr[idx_k] = temp_left[idx_i]
            idx_i += 1
        else:
            arr[idx_k] = temp_right[idx_j]
            idx_j += 1
        idx_k += 1

    # Copy the remaining elements of temp_left, if any.
    while idx_i < len_left_arr:
        arr[idx_k] = temp_left[idx_i]
        idx_i += 1
        idx_k += 1

    # Copy the remaining elements of temp_right, if any.
    while idx_j < len_right_arr:
        arr[idx_k] = temp_right[idx_j]
        idx_j += 1
        idx_k += 1
