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

test_suite = unittest.TestLoader().loadTestsFromTestCase(TestUtilClustering)
unittest.TextTestRunner(verbosity=2).run(test_suite)
# Run in terminal with: python ./util_clustering.spec.py