"""
Example code for creating and visualizing
cluster of county-based cancer risk data

Note that you must download the file
http://www.codeskulptor.org/#alg_clusters_matplotlib.py
to use the matplotlib version of this code
"""

# Flavor of Python - desktop or CodeSkulptor
DESKTOP = True

import math
import random
import copy
import urllib2
import alg_cluster
from matplotlib import pyplot

# conditional imports
# if DESKTOP:
import util_clustering as alg_project3_solution     # desktop project solution
import alg_clusters_matplotlib
# else:
# import userXX_XXXXXXXX as alg_project3_solution   # CodeSkulptor project solution
# import alg_clusters_simplegui
# import codeskulptor
# codeskulptor.set_timeout(30)


###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib2.urlopen(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])]
            for tokens in data_tokens]


############################################################
# Code to create sequential clustering
# Create alphabetical clusters for county data

def sequential_clustering(singleton_list, num_clusters):
    """
    Take a data table and create a list of clusters
    by partitioning the table into clusters based on its ordering

    Note that method may return num_clusters or num_clusters + 1 final clusters
    """

    cluster_list = []
    cluster_idx = 0
    total_clusters = len(singleton_list)
    cluster_size = float(total_clusters) / num_clusters

    for cluster_idx in range(len(singleton_list)):
        new_cluster = singleton_list[cluster_idx]
        if math.floor(cluster_idx / cluster_size) != \
           math.floor((cluster_idx - 1) / cluster_size):
            cluster_list.append(new_cluster)
        else:
            cluster_list[-1] = cluster_list[-1].merge_clusters(new_cluster)

    return cluster_list


#####################################################################
# Code to load cancer data, compute a clustering and
# visualize the results


def run_example():
    """
    Load a data table, compute a list of clusters and 
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    data_table = load_data_table(DATA_111_URL)
    singleton_list = generate_singleton_list(data_table)

    # cluster_list = sequential_clustering(singleton_list, 15)
    # print "Displaying", len(cluster_list), "sequential clusters"

    cluster_list = alg_project3_solution.hierarchical_clustering(
        singleton_list, 9)
    # print "Displaying", len(cluster_list), "hierarchical clusters"

    # cluster_list = alg_project3_solution.kmeans_clustering(
    #     singleton_list, 9, 5)
    # print "Displaying", len(cluster_list), "k-means clusters"

    distortion = alg_project3_solution.compute_distortion(
        cluster_list, data_table)
    print('Distortion equals ' + str(distortion))

    # draw the clusters using matplotlib or simplegui
    # if DESKTOP:
    # alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)
    # alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)  #add cluster centers
    # else:
    #     # use toggle in GUI to add cluster centers
    #     alg_clusters_simplegui.PlotClusters(data_table, cluster_list)


def generate_singleton_list(data_table):
    """
    Generate a list of Cluster objects from the provided URL.

    @param list County data.

    @return list Cluster objects.
    """
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(
            set([line[0]]), line[1], line[2], line[3], line[4]))

    return singleton_list


def compare_distortion(data_url, num_data_points):
    """
    Compute the distortion of the list of clusters provided by the hierarchical
    clustering and k-means clustering algorithms on the 111, 290, and 896
    county data sets where the number of output clusters ranges from 6-20.

    @param string URL of the data table.
    @param int Count of data points in the table.
    """
    NUM_KMEANS_ITERATIONS = 5
    MAX_CLUSTER_SIZE = 20
    MIN_CLUSTER_SIZE = 6

    data_table = load_data_table(data_url)

    # Calculate hierarchical clustering distortion.
    distortion_by_cluster_size = []
    cluster_list = generate_singleton_list(data_table)
    for cluster_size in range(MAX_CLUSTER_SIZE, MIN_CLUSTER_SIZE - 1, -1):
        cluster_list = alg_project3_solution.hierarchical_clustering(
            cluster_list, cluster_size)
        distortion = alg_project3_solution.compute_distortion(
            cluster_list, data_table)
        distortion_by_cluster_size.append((cluster_size, distortion))

    # Plot hierarchical clustering distortion.
    x = []
    y = []
    for distortion_entry in distortion_by_cluster_size:
        x.append(distortion_entry[0])
        y.append(distortion_entry[1])
    pyplot.plot(x, y, label='hierarchical')

    # Calculate k-means clustering distortion.
    distortion_by_cluster_size = []
    singleton_list = generate_singleton_list(data_table)
    for cluster_size in range(MAX_CLUSTER_SIZE, MIN_CLUSTER_SIZE - 1, -1):
        cluster_list = alg_project3_solution.kmeans_clustering(
            copy.deepcopy(singleton_list), cluster_size, NUM_KMEANS_ITERATIONS)
        distortion = alg_project3_solution.compute_distortion(
            cluster_list, data_table)
        distortion_by_cluster_size.append((cluster_size, distortion))

    # Plot k-means clustering distortion.
    x = []
    y = []
    for distortion_entry in distortion_by_cluster_size:
        x.append(distortion_entry[0])
        y.append(distortion_entry[1])
    pyplot.plot(x, y, label='k-means')

    # Configure plot.
    pyplot.legend(loc='upper right')
    pyplot.title('Clustering Distortion for ' + str(num_data_points) +
                 ' Points')
    pyplot.xlabel('Cluster Size')
    pyplot.ylabel('Distortion x 10^11 (sum of squares distance)')

    # Show plot.
    pyplot.show()


def main():
    compare_distortion(DATA_896_URL, 896)


# Call main.
if __name__ == '__main__':
    main()
