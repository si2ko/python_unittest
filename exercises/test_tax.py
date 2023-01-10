
import unittest

from tax import calc_tax

class TestCalcTax(unittest.TestCase):

    def testcase1(self):

        self.assertEqual(10, calc_tax(100,10))


 def testcase2(self):

     self.assertRaises(TypeError, calc_tax, 1000,1,'stt')
     self.assertRaises(ValueError, calc_tax, 1000,1,-1)

