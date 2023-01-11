import unittest
import sys

from employee import Employee


class EmployeeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setting up')
        cls.emp = Employee('John','Smith',80000)

    @classmethod
    def tearDownClass(cls):
        print('tearing down...')
        del cls.emp

    def test_case1(self):

        self.assertEqual('john.smith@email.com', self.emp.email)







