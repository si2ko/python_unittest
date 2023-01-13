import unittest
from parameterized import parameterized

from calc_math import SimpleMathCalculator


class TestSimpleMathCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleMathCalculator()

    @parameterized.expand([('positive',-3,-2,-5),
                           ('negative',2,2,5)
                           ])
    def test_add(self,name,x ,y, result):

        self.assertEqual(self.calc.add(x,y), result)