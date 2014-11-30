# coding: utf8

from vbench.benchmark import Benchmark

setup = """
from __future__ import division

import dit
from itertools import product

outcomes = list(product(['0', '1', '2'], repeat=3))
pmf = np.array([1/27] * 27)

"""

code = """
d = dit.Distribution(outcomes, pmf)
"""

bm = Benchmark(code, setup, name='initdist')

