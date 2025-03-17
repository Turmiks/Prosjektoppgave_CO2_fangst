import unittest

from ..constants3 import *
from ..thermodynamics import *


class TestHeatCapacity(unittest.TestCase):

    def test_heat_capacity(self):
        coeff_w: list = [5.0536, -5.6552e-3,9.1400e-6]
        temp: float = 298
        self.assertAlmostEqual(heat_capacity(temp, coeff_w), 4.18)