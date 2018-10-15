"""
Test suite for the clustering efficiency utility.
"""
import unittest
import util_cluster_efficiency


class TestUtilClusterEfficiency(unittest.TestCase):
    """
    Unit tests for clustering efficiency utility.
    Each test method must begin with "test_".
    """

    def setUp(self):
        """
        Run before each test.
        """
        pass

    def test_gen_random_clusters(self):
        self.assertEqual(
            len(util_cluster_efficiency.gen_random_clusters(-2)), 0)
        self.assertEqual(len(util_cluster_efficiency.gen_random_clusters(0)), 0)
        self.assertEqual(len(util_cluster_efficiency.gen_random_clusters(2)), 2)


test_suite = unittest.TestLoader().loadTestsFromTestCase(
    TestUtilClusterEfficiency)
unittest.TextTestRunner(verbosity=2).run(test_suite)
