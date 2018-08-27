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
    @param float Maximal distance of any point in the strip from horiz_center.

    @return tuple (dist, idx1, idx2) Dist is the distance between the closest
      pair of clusters in the strip array.
    """
    # Build an array, strip_arr, that contains points closer than half_width to,
    # horiz_center, the line passing through the middle point.
    # Maintain the original index in the cluster list as part of each item
    # within strip_arr in order to return this value.
    strip_arr = []
    for idx_i in range(len(cluster_list)):
        if(abs(cluster_list[idx_i].horiz_center() - horiz_center) < half_width):
            strip_arr.append([idx_i, cluster_list[idx_i]])

    len_k = len(strip_arr)
    # Sort strip_arr by y-coordinates.
    merge_sort(strip_arr, 0, len_k - 1, compare_y)

    min_distance = half_width
    d_i_j = (min_distance, -1, -1)
    # Pick all points one-by-one and compare to the distance from the adjacent
    # point until the difference between y-coordinates/vert_center is smaller
    # than the minimum distance.
    # The loop will run at most six times due to the fact the distance between
    # the two y-coordinates will be bounded by a height of 2*min_distance and
    # width of 1*min_distance.
    for idx_u in range(len_k - 1):
        for idx_v in range(min(idx_u + 4, len_k)):
            dist = strip_arr[idx_u][1].distance(strip_arr[idx_v][1])
            if dist < d_i_j[0]:
                d_i_j = (dist, strip_arr[idx_u][0], strip_arr[idx_v][0])

    return d_i_j


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


def merge_sort(arr, left, right, comparison_func):
    """
    Divide and conquer algorithm for sorting elements in a stable fashion.

    @param array Elements to sort.
    @param int First index of the left half of the array.
    @param int Last index of the right half of the array.
    @param func Compares the array items.
    """
    if left < right:
        middle = (left + right) // 2

        # Sort first and second halves.
        merge_sort(arr, left, middle, comparison_func)
        merge_sort(arr, middle + 1, right, comparison_func)
        merge(arr, left, middle, right, comparison_func)


def merge(arr, left, middle, right, comparison_func):
    """
    Merge the two subarrays of arr. 
    The first subarray is arr[left:middle].
    The second subarray is arr[middle+1:right]

    @param array Elements of the subarrays.
    @param int First index of the left subarray.
    @param int Middle index of the array.
    @param int Last index of the right subarray.
    @param func Compares the array items.
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
        if comparison_func(temp_left[idx_i], temp_right[idx_j]) <= 0:
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


def compare_y(cluster_1, cluster_2):
    """
    Compare Y coordinates between two Cluster objects.

    @param array [idx in list, Cluster to compare]
    @param array [idx, in list, Cluster to compare]

    @return int Positive if cluster_1 is greater than cluster_2.
        Negative if cluster_2 is greater than cluster_1.
        Zero is the clusters are equal.
    """
    return cluster_1[1].vert_center() - cluster_2[1].vert_center()
