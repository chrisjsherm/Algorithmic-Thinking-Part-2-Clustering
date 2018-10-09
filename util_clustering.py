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
    @param float Horizontal position of the two points in the middle of the 
        cluster.
    @param float Maximal distance of any point in the strip from horiz_center.

    @return tuple (dist, idx1, idx2) Dist is the distance between the closest
      pair of clusters in the strip array.
    """
    # Build an array, strip_arr, that contains points closer than half_width to
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

    d_i_j = (float('inf'), -1, -1)
    # Pick all points one-by-one and compare to the distance from the adjacent
    # point until the difference between y-coordinates/vert_center is smaller
    # than the minimum distance.
    # The loop will run at most six times due to the fact the distance between
    # the two y-coordinates will be bounded by a height of 2*half_width and a
    # width of 1*half_width.
    for idx_u in range(len_k - 1):
        for idx_v in range(idx_u + 1, min(idx_u + 4, len_k)):
            dist = strip_arr[idx_u][1].distance(strip_arr[idx_v][1])
            if dist < d_i_j[0]:
                temp_sorted_idx = [strip_arr[idx_u][0], strip_arr[idx_v][0]]
                temp_sorted_idx.sort()
                d_i_j = (dist, temp_sorted_idx[0], temp_sorted_idx[1])

    return d_i_j


def fast_closest_pair(cluster_list):
    """
    Clusters passed to fast_closest_pair must be in horizontal sorted order.
    Takes a list of Cluster objects and returns a closest pair where the pair is
    represented by a tuple (dist, idx1, idx2) with idx1 < idx2 where dist is the
    distance between the closest pair cluster_list[idx1] and cluster_list[idx2].
    This is a divide and conquer algorithm.

    @param list List of Cluster objects.

    @return tuple (dist, idx1, idx2) Dist is the distance between the closest
      pair in the cluster_list parameter. idx1 and idx2 represent 
      cluster_list[idx1], cluster_list[idx2].
    """
    list_len = len(cluster_list)

    # If there are less than four points, use brute force algorithm.
    if list_len <= 3:
        return slow_closest_pair(cluster_list)

    # Identify the middle index of the cluster list.
    middle_idx = int(round(list_len / 2))

    # Calculate the closest pair on the left half of the list.
    closest_pair_left = fast_closest_pair(cluster_list[0:middle_idx])

    # Calculate the closest pair on the right half of the list.
    closest_pair_right = fast_closest_pair(
        cluster_list[middle_idx:list_len])

    # Adjust indices on the right side of list.
    closest_pair_right = (
        closest_pair_right[0], closest_pair_right[1] + middle_idx, closest_pair_right[2] + middle_idx)

    closest_pair = min(
        [closest_pair_left, closest_pair_right], key=lambda x: x[0])
    horiz_center = (cluster_list[middle_idx - 1].horiz_center() +
                    cluster_list[middle_idx].horiz_center()) / 2
    stripped_closest_pair = closest_pair_strip(
        cluster_list, horiz_center, closest_pair[0])

    closest_pair = min(
        [closest_pair, stripped_closest_pair], key=lambda x: x[0])

    return closest_pair


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
    @param array [idx in list, Cluster to compare]

    @return int Positive if cluster_1 is greater than cluster_2.
        Negative if cluster_2 is greater than cluster_1.
        Zero is the clusters are equal.
    """
    return cluster_1[1].vert_center() - cluster_2[1].vert_center()


def compare_x(cluster_1, cluster_2):
    """
    Compare X coordinates between two Cluster objects.

    @param Cluster Cluster to compare.
    @param Cluster Cluster to compare.

    @return int Positive if cluster_1's x-coordinate is greater than cluster_2's.
        Negative if cluster_2's x-coordinate is greater than cluster_1's.
        Zero if the cluster's x-coordinates are equal.
    """
    return cluster_1.horiz_center() - cluster_2.horiz_center()


def are_clusters_equal(cluster_1, cluster_2):
    """
    Compare two Cluster objects to see if they have identical property values.

    @param Cluster Cluster to compare.
    @param Cluster Cluster to compare.

    @return boolean True if the clusters have identical property values.
        False otherwise.
    """
    if cluster_1 == None or cluster_2 == None:
        return False

    if cluster_1.fips_codes() == cluster_2.fips_codes() and \
            cluster_1.horiz_center() == cluster_2.horiz_center() and \
            cluster_1.vert_center() == cluster_2.vert_center() and \
            cluster_1.total_population() == cluster_2.total_population() and \
            cluster_1.averaged_risk() == cluster_2.averaged_risk():
        return True

    return False


def are_cluster_lists_equal(cluster_list_1, cluster_list_2):
    """
    Compare two lists of Cluster objects to see if they contain Cluster objects
    with identical property values.

    @param Cluster List of Clusters to compare.
    @param Cluster List of Clusters to compare.

    @return boolean True the lists contain Cluster objects with identical values.
        False otherwise.
    """
    if len(cluster_list_1) != len(cluster_list_2):
        return False

    for idx in range(len(cluster_list_1)):
        if not are_clusters_equal(cluster_list_1[idx], cluster_list_2[idx]):
            return False

    return True


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Takes a list of Cluster objects and applies the hierarchical clustering
    algorithm. The clustering process proceeds until num_clusters remain.

    @param array Cluster objects.
    @param int Number of clusters to condense cluster_list into.

    @return array Cluster objects.
    """
    # Clusters passed to fast_closest_pair must be in horizontal sorted order.
    merge_sort(cluster_list, 0, len(cluster_list) - 1, compare_x)

    while len(cluster_list) > num_clusters:
        # Find the closest pair of clusters
        closest_pair = fast_closest_pair(cluster_list)

        # Grab the second cluster of the pair from cluster_list.
        cluster_to_merge = cluster_list[closest_pair[2]]

        # Merge the closest pair of clusters.
        cluster_list[closest_pair[1]].merge_clusters(cluster_to_merge)

        # Remove the second cluster of the pair from cluster_list.
        cluster_list.pop(closest_pair[2])

    return cluster_list


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Takes a list of Cluster objects and applies the k-means clustering algorithm.

    @param list Cluster objects.
    @param int Number of clusters to condense cluster_list into.
    @param int Number of iterations to perform the k-means clustering algorithm.

    @return list Cluster objects.
    """
    n_clusters = len(cluster_list)

    # Ensure the size of cluster_list is at least equal to the number of
    # clusters to create.
    if n_clusters < num_clusters:
        raise ValueError('num_clusters must be less than or equal to the ' +
                         'length of cluster_list.')

    # Initialize the old clusters by selecting the largest population counties.
    old_clusters = sorted(
        cluster_list, key=lambda x: x.total_population(), reverse=True)[:num_clusters]

    # Perform the k-means algorithm for the supplied number of iterations.
    for dummy_iter in range(0, num_iterations):
        # Initialize groups to add clusters to.
        cluster_groups = [[] for dummy_idx in range(0, num_clusters)]

        # For each county in cluster_list.
        for idx_j in range(0, n_clusters):
            # Find the old cluster center that is closest to the current county.
            closest_cluster_idx = min_dist_to_cluster(
                old_clusters, cluster_list[idx_j])

            # Add the county to the corresponding cluster_group.
            cluster_groups[closest_cluster_idx].append(cluster_list[idx_j])

        # Transform the cluster_groups into new clusters.
        for idx_i in range(0, num_clusters):
            # Create a new Cluster from the first cluster in the group.
            new_cluster = cluster_groups[idx_i][0].copy()

            # If more than one cluster in a group, merge into the first
            # cluster in the group.
            for idx_j in range(1, len(cluster_groups[idx_i])):
                new_cluster.merge_clusters(
                    cluster_groups[idx_i][idx_j])

            # Set the cluster group equal to the first cluster.
            cluster_groups[idx_i] = new_cluster

        # Set the old clusters equal to the new clusters.
        old_clusters = cluster_groups

    # Return the new clusters.
    return old_clusters


def min_dist_to_cluster(cluster_list, compare_cluster):
    """
    Takes a list of clusters and returns the index with the minimum distance
    to the compare_cluster.

    @param list Cluster objects.
    @param Cluster Cluster to compare the list to.

    @return int Index of the Cluster with the minimum distance to the
        compare_cluster.
    """
    min_dist = float('inf')
    idx = -1
    for idx_i in range(0, len(cluster_list)):
        dist = cluster_list[idx_i].distance(compare_cluster)
        if dist < min_dist:
            min_dist = dist
            idx = idx_i

    return idx
