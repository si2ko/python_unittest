import unittest

def rectangle(width, height):
    """Function that calculate area of rectanlge"""

    if not (isinstance(width,(int,float)) and isinstance(height,(int, float))):
        raise TypeError('Instances must be int or float type')

    if not (height > 0 and width > 0):
        raise ValueError('Instances must be above zero')

    return width * height

class TestRectangle(unittest.TestCase):

    def test_rectangle(self):

        self.assertEqual(rectangle(5,4),20)

    def test_rectangle_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, rectangle, '4', 5)
        self.assertRaises(TypeError, rectangle, 4, '5')

    def test_rectangle_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, rectangle, -4, 5)
        self.assertRaises(ValueError, rectangle, 4, -5)

if __name__ == '__main__':
    unittest.main(verbosity=2)
