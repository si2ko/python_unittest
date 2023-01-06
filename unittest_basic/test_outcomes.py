import unittest

def rectangle(width, height):
    """Function that calculate area of rectanlge"""

    if not (isinstance(width,(int,float)) and isinstance(height,(int, float))):
        raise TypeError('Instances must be int or float type')

    if not (height > 0 and width > 0):
        raise ValueError('Instances must be above zero')

    return width * height

class TestRectangle(unittest.TestCase):

    def test_rectangle_1(self):
        self.assertEqual(rectangle(5,4),20)

    def test_rectangle_2 (self):
        self.assertEqual(rectangle(5,4),21)

    def test_rectangle_3 (self):
        raise AssertionError('Error message')

    def test_rectangle_4 (self):
        raise TypeError('Error message')


if __name__ == '__main__':
    unittest.main(verbosity=2)
