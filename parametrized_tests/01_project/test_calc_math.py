import unittest

from calc_math import SimpleMathCalculator


class TestSimpleMathCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleMathCalculator()

    def test_add1(self):

        self.assertEqual(self.calc.add(-4,-2),-6)
        self.assertEqual(self.calc.add(-4, 2), -2)
        self.assertEqual(self.calc.add(4, -2), 2)
        self.assertEqual(self.calc.add(4, 2), 6)