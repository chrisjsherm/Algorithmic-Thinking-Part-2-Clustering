"""
Test suite for the clustering utility.
"""
import unittest
import math
from alg_cluster import Cluster
import util_clustering


class TestUtilClustering(unittest.TestCase):
    """
    Unit tests for clustering utility.
    """

    def setUp(self):
        """
        Run before each test.
        Each test method must begin with "test_".
        """
        cluster1 = Cluster(set([32001, 32013, 32031]), 2, 2, 400, .1)
        cluster2 = Cluster(set([51121, 51155, 51161]), 0, 0, 600, .2)
        cluster3 = Cluster(set([51059, 51013, 51107]), -2, -2, 800, .3)
        self._cluster_list = [cluster1, cluster2, cluster3]
        self._compare_func = lambda x1, x2: x1 - x2

    def test_slow_closest_pair(self):
        self.assertEqual(util_clustering.slow_closest_pair(
            self._cluster_list), (math.sqrt(8), 0, 1))

        cluster_list_2 = [Cluster(set([]), 0.38, 0.26, 1, 0),
                          Cluster(set([]), 0.42, 0.03, 1, 0),
                          Cluster(set([]), 0.48, 0.23, 1, 0),
                          Cluster(set([]), 0.8, 0.65, 1, 0),
                          Cluster(set([]), 0.95, 0.85, 1, 0),
                          Cluster(set([]), 0.97, 0.61, 1, 0)]
        self.assertEqual(util_clustering.slow_closest_pair(
            cluster_list_2), (0.10440306508910548, 0, 2))

        cluster_list_3 = [Cluster(set([]), 0.38, 0.26, 1, 0),
                          Cluster(set([]), 0.42, 0.03, 1, 0)]
        self.assertEqual(util_clustering.slow_closest_pair(
            cluster_list_3), (0.23345235059857505, 0, 1))

    def test_closest_pair_strip(self):
        self.assertEqual(util_clustering.closest_pair_strip(
            self._cluster_list, -1, 2), (math.sqrt(8), 1, 2))

        cluster1 = Cluster([51121, 51155, 51161], -7, 3, 600, .2)
        cluster2 = Cluster([51059, 51013, 51107], -1, 1, 800, .3)
        cluster3 = Cluster([51121, 51155, 51161], 3, 6, 600, .2)
        cluster4 = Cluster([32001, 32013, 32031], 3, 5, 400, .1)
        cluster5 = Cluster([32001, 32013, 32031], 4, 6, 400, .1)
        cluster_list_2 = [cluster1, cluster2, cluster3, cluster4, cluster5]
        self.assertEqual(util_clustering.closest_pair_strip(
            cluster_list_2, 2, math.sqrt(2)), (1.0, 2, 3))

    def test_fast_closest_pair(self):
        self.assertEqual(util_clustering.fast_closest_pair(
            self._cluster_list), (math.sqrt(8), 0, 1))

        cluster1 = Cluster([51121, 51155, 51161], -7, 3, 600, .2)
        cluster2 = Cluster([51059, 51013, 51107], -1, 1, 800, .3)
        cluster3 = Cluster([51121, 51155, 51161], 3, 6, 600, .2)
        cluster4 = Cluster([32001, 32013, 32031], 3, 5, 400, .1)
        cluster5 = Cluster([32001, 32013, 32031], 4, 6, 400, .1)
        cluster_list_2 = [cluster1, cluster2, cluster3, cluster4, cluster5]
        self.assertEqual(util_clustering.fast_closest_pair(
            cluster_list_2), (1.0, 2, 3))

        cluster_list_3 = [Cluster(set([]), 0.38, 0.26, 1, 0),
                          Cluster(set([]), 0.42, 0.03, 1, 0),
                          Cluster(set([]), 0.48, 0.23, 1, 0),
                          Cluster(set([]), 0.8, 0.65, 1, 0),
                          Cluster(set([]), 0.95, 0.85, 1, 0),
                          Cluster(set([]), 0.97, 0.61, 1, 0)]
        self.assertEqual(util_clustering.fast_closest_pair(
            cluster_list_3), (0.10440306508910548, 0, 2))

    def test_merge(self):
        arr1 = [11, 12, 13, 5, 6, 7]
        util_clustering.merge(arr1, 0, (len(arr1) - 1) // 2, len(arr1) - 1,
                              self._compare_func)
        self.assertListEqual(arr1, [5, 6, 7, 11, 12, 13])

        arr2 = [1, 3, 4, 7, 9]
        util_clustering.merge(arr2, 0, (len(arr2) - 1) // 2, len(arr2) - 1,
                              self._compare_func)
        self.assertListEqual(arr2, [1, 3, 4, 7, 9])

        jordan = [23]
        util_clustering.merge(jordan, 0, (len(jordan) - 1) // 2, len(jordan) - 1,
                              self._compare_func)
        self.assertListEqual(jordan, [23])

    def test_merge_sort(self):
        arr1 = [12, 11, 13, 5, 6, 7]
        util_clustering.merge_sort(arr1, 0, len(arr1) - 1,
                                   self._compare_func)
        self.assertListEqual(arr1, [5, 6, 7, 11, 12, 13])

        arr2 = [4, 1, 3, 9, 7]
        util_clustering.merge_sort(arr2, 0, len(arr2) - 1,
                                   self._compare_func)
        self.assertListEqual(arr2, [1, 3, 4, 7, 9])

        arr3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        util_clustering.merge_sort(arr3, 0, len(arr3) - 1,
                                   self._compare_func)
        self.assertListEqual(arr3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        arr4 = [54, 3, 44, 69, 101, 5, 18, 21]
        util_clustering.merge_sort(arr4, 0, len(arr4) - 1,
                                   self._compare_func)
        self.assertListEqual(arr4, [3, 5, 18, 21, 44, 54, 69, 101])

        jordan = [23]
        util_clustering.merge_sort(jordan, 0, len(jordan) - 1,
                                   self._compare_func)
        self.assertListEqual(jordan, [23])

    def test_compare_y(self):
        cluster_1 = [1, Cluster([22152], -2, 2, 0, 0)]
        cluster_2 = [3, Cluster([90210], 0, 0, 0, 0)]
        self.assertEqual(util_clustering.compare_y(cluster_1, cluster_2), 2)

        cluster_1 = [0, Cluster([22152], -2, 2, 0, 0)]
        cluster_2 = [5, Cluster([90210], 0, 2, 0, 0)]
        self.assertEqual(util_clustering.compare_y(cluster_1, cluster_2), 0)

        cluster_1 = [2, Cluster([22152], -2, -4, 0, 0)]
        cluster_2 = [4, Cluster([90210], 0, 2, 0, 0)]
        self.assertEqual(util_clustering.compare_y(cluster_1, cluster_2), -6)

    def test_compare_x(self):
        cluster_1 = Cluster([22152], -2, 2, 0, 0)
        cluster_2 = Cluster([90210], 0, 0, 0, 0)
        self.assertEqual(util_clustering.compare_x(cluster_1, cluster_2), -2)

        cluster_1 = Cluster([22152], -2, 2, 0, 0)
        cluster_2 = Cluster([90210], -2, 2, 0, 0)
        self.assertEqual(util_clustering.compare_x(cluster_1, cluster_2), 0)

        cluster_1 = Cluster([22152], -2, -4, 0, 0)
        cluster_2 = Cluster([90210], -4, 2, 0, 0)
        self.assertEqual(util_clustering.compare_x(cluster_1, cluster_2), 2)

    def test_are_clusters_equal(self):
        self.assertFalse(util_clustering.are_clusters_equal(
            self._cluster_list[0], self._cluster_list[1]))

        self.assertFalse(util_clustering.are_clusters_equal(self._cluster_list[0],
                                                            Cluster(set([32001, 32013, 32041]), 2, 2, 400, .1)))

        self.assertFalse(util_clustering.are_clusters_equal(self._cluster_list[0],
                                                            Cluster(set([32001, 32013, 32041]), 3, 2, 400, .1)))

        self.assertFalse(util_clustering.are_clusters_equal(self._cluster_list[0],
                                                            Cluster(set([32001, 32013, 32041]), 3, 5, 400, .1)))

        self.assertFalse(util_clustering.are_clusters_equal(self._cluster_list[0],
                                                            Cluster(set([32001, 32013, 32041]), 3, 2, 425, .1)))

        self.assertFalse(util_clustering.are_clusters_equal(self._cluster_list[0],
                                                            Cluster(set([32001, 32013, 32041]), 3, 2, 400, 1.1)))

        self.assertTrue(util_clustering.are_clusters_equal(
            self._cluster_list[0], Cluster(set([32001, 32013, 32031]), 2, 2, 400, .1)))

    def test_are_cluster_lists_equal(self):
        self.assertFalse(util_clustering.are_cluster_lists_equal(
            self._cluster_list,
            [Cluster(set([32001, 32133, 32031]), 2, 2, 400, .1),
             Cluster(set([51121, 51155, 51161]), 0, 0, 600, .2),
             Cluster(set([51059, 51013, 51107]), -2, -2, 800, .3)]))

        self.assertFalse(util_clustering.are_cluster_lists_equal(
            self._cluster_list,
            [Cluster(set([32001, 32013, 32031]), 2, 2, 400, .1),
             Cluster(set([51121, 51155, 51161]), 0, 0, 600, .2),
             Cluster(set([51059, 51013, 51107]), -2, -2, 1200, .3)]))

        self.assertFalse(util_clustering.are_cluster_lists_equal(
            self._cluster_list,
            [Cluster(set([51121, 51155, 51161]), -7, 3, 600, .2),
             Cluster(set([32001, 32013, 32031]), 2, 2, 400, .1),
             Cluster(set([51121, 51155, 51161]), 0, 0, 600, .2),
             Cluster(set([51059, 51013, 51107]), -2, -2, 800, .3)]))

        self.assertTrue(util_clustering.are_cluster_lists_equal(
            self._cluster_list,
            [Cluster(set([32001, 32013, 32031]), 2, 2, 400, .1),
             Cluster(set([51121, 51155, 51161]), 0, 0, 600, .2),
             Cluster(set([51059, 51013, 51107]), -2, -2, 800, .3)]))

    def test_min_dist_to_cluster(self):
        compare_cluster = Cluster(set([22140, 22141, 22142]), 3, 3, 400, .1)
        self.assertEqual(util_clustering.min_dist_to_cluster(
            self._cluster_list, compare_cluster), 0
        )


test_suite = unittest.TestLoader().loadTestsFromTestCase(TestUtilClustering)
unittest.TextTestRunner(verbosity=2).run(test_suite)
# Run in terminal with: python ./util_clustering.spec.py
