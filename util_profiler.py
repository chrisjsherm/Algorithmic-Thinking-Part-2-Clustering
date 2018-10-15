"""
Utility functions for performance profiling.
"""
import timeit
from functools import partial
from matplotlib import pyplot


def plot_time_complexity(fn, n_min, n_max, n_incr, n_tests):
    """
    Run timer and plot time complexity.

    @param func Function to profile.
    @param int Starting value of N.
    @param int Ending value of N (not inclusive).
    @param int Step incrementer of N.
    @param int Number of times to run each test (helps avoid outliers).
    """
    x = []
    y = []
    for i in range(n_min, n_max, n_incr):
        N = i
        test_n_time = timeit.Timer(partial(fn, N))
        time_sec = test_n_time.timeit(number=n_tests)
        x.append(i)
        y.append(time_sec)

    pyplot.plot(x, y, label=fn.__name__)
