"""
Answers to questions for Application 3 of Algorithmic Thinking.
"""
from util_cluster_efficiency import gen_random_clusters
from util_clustering import slow_closest_pair, fast_closest_pair
from util_profiler import plot_time_complexity
from matplotlib import pyplot


def slow_closest_pair_trial(N):
    """
    Call the slow_closest_pair algorithm implementation from util_clustering and
    profile the running time.

    @param int Number of Clusters to the function should execute with.
    """
    slow_closest_pair(gen_random_clusters(N))


def fast_closest_pair_trial(N):
    """
    Call the fast_closest_pair algorithm implementation from util_clustering and
    profile the running time.

    @param int Number of Clusters to the function should execute with.
    """
    fast_closest_pair(gen_random_clusters(N))


def main():
    n_min = 2
    n_max = 200
    n_incr = 1
    n_tests = 3

    plot_time_complexity(slow_closest_pair_trial, n_min, n_max, n_incr, n_tests)
    plot_time_complexity(fast_closest_pair_trial, n_min, n_max, n_incr, n_tests)

    # show plot
    pyplot.legend(loc='upper right')
    pyplot.show()


# call main
if __name__ == '__main__':
    main()
