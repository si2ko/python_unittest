import unittest

from calc_math import SimpleMathCalculator




class TestSimpleMathCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setting up...')
        cls.calc = SimpleMathCalculator()
    @classmethod
    def tearDownClass(cls):
        print('tearing down...')
        del cls.calc

    def test_add(self):

        self.assertEqual(self.calc.add(2,2),4)


    def test_sub(self):


        self.assertEqual(self.calc.sub(2, 2), 0)


    def test_mul(self):


        self.assertEqual(self.calc.mul(2, 2), 4)


