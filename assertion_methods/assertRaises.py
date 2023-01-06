import unittest


def get_value(index, container):
    return container[index]

class TestClass(unittest.TestCase):

    def test_case_1(self):

        self.assertRaises(IndexError, get_value, 4 ,'aws')

    def test_case_2(self):

        with self.assertRaises(IndexError):
            get_value(3,'aws')


