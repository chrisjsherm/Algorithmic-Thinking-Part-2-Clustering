"""
Test suite for the clustering utility.
"""
import unittest
import util_clustering
from alg_cluster import Cluster
import util_clustering
import math


class TestUtilClustering(unittest.TestCase):
    """
    Unit tests for clustering utility.
    """

    def setUp(self):
        """
        Run before each test.
        Each test method must begin with "test_".
        """
        cluster1 = Cluster([32001, 32013, 32031], 2, 2, 400, .1)
        cluster2 = Cluster([51121, 51155, 51161], 0, 0, 600, .2)
        cluster3 = Cluster([51059, 51013, 51107], -2, -2, 800, .3)
        self._cluster_list = [cluster1, cluster2, cluster3]

    def test_slow_closest_pair(self):
        self.assertEqual(util_clustering.slow_closest_pair(
            self._cluster_list), (math.sqrt(8), 0, 1))

    def test_closest_pair_strip(self):
        self.assertEqual(util_clustering.closest_pair_strip(
            self._cluster_list, 0, 1), (float('inf'), -1, -1))

    def test_fast_closest_pair(self):
        self.assertEqual(util_clustering.fast_closest_pair(
            self._cluster_list), (math.sqrt(8), 0, 1))

    def test_merge(self):
        arr1 = [11, 12, 13, 5, 6, 7]
        util_clustering.merge(arr1, 0, (len(arr1) - 1) // 2, len(arr1) - 1)
        self.assertListEqual(arr1, [5, 6, 7, 11, 12, 13])

        arr2 = [1, 3, 4, 7, 9]
        util_clustering.merge(arr2, 0, (len(arr2) - 1) // 2, len(arr2) - 1)
        self.assertListEqual(arr2, [1, 3, 4, 7, 9])

        jordan = [23]
        util_clustering.merge(jordan, 0, (len(jordan) - 1) // 2, len(jordan) - 1)
        self.assertListEqual(jordan, [23])

    def test_merge_sort(self):
        arr1 = [12, 11, 13, 5, 6, 7]
        util_clustering.merge_sort(arr1, 0, len(arr1) - 1)
        self.assertListEqual(arr1, [5, 6, 7, 11, 12, 13])

        arr2 = [4, 1, 3, 9, 7]
        util_clustering.merge_sort(arr2, 0, len(arr2) - 1)
        self.assertListEqual(arr2, [1, 3, 4, 7, 9])

        arr3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        util_clustering.merge_sort(arr3, 0, len(arr3) - 1)
        self.assertListEqual(arr3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        arr4 = [54, 3, 44, 69, 101, 5, 18, 21]
        util_clustering.merge_sort(arr4, 0, len(arr4) - 1)
        self.assertListEqual(arr4, [3, 5, 18, 21, 44, 54, 69, 101])
        
        jordan = [23]
        util_clustering.merge_sort(jordan, 0, len(jordan) - 1)
        self.assertListEqual(jordan, [23])


test_suite = unittest.TestLoader().loadTestsFromTestCase(TestUtilClustering)
unittest.TextTestRunner(verbosity=2).run(test_suite)
# Run in terminal with: python ./util_clustering.spec.py
