import unittest

from rectangle import rectangle, perimeter

class TestRectangle(unittest.TestCase):

    def test_rectangle(self):

        self.assertEqual(rectangle(5,4),20)

    def test_rectangle_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, rectangle, '4', 5)
        self.assertRaises(TypeError, rectangle, 4, '5')

    def test_rectangle_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, rectangle, -4, 5)
        self.assertRaises(ValueError, rectangle, 4, -5)

class TestPerimeter(unittest.TestCase):

    def test_perimeter(self):

        self.assertEqual(perimeter(5,4),18)

    def test_perimeter_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, perimeter, '4', 5)
        self.assertRaises(TypeError, perimeter, 4, '5')

    def test_perimeter_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, perimeter, -4, 5)
        self.assertRaises(ValueError, perimeter, 4, -5)

    