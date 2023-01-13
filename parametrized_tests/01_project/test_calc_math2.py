import unittest

from calc_math import SimpleMathCalculator


class TestSimpleMathCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleMathCalculator()



    def test_add(self):

        cases = [
            (-4,-2,-6),
            (-4,2,-2),
            (4,-2,0),
            (4,2,6)
        ]
        for x,y, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(self.calc.add(x,y),result)