import unittest
import sys

from employee import Employee

class EmployeeTest(unittest.TestCase):

    def setUp(self):
        print('setting up...')
        self.emp = emp = Employee('John', 'Smith', 80000)

    def tearDown(self):
        print('tearing down...')

    def test_email(self):

        self.assertEqual('john.smith@email.com', self.emp.email)

    def test_if_last_name_change(self):

        self.emp.last_name = 'Dow'
        self.assertEqual('john.dow@email.com', self.emp.email)

    def test_if_first_name_change(self):

        self.emp.first_name = 'Jack'
        self.assertEqual('jack.smith@email.com', self.emp.email)

    def test_tax(self):

        self.assertAlmostEqual(13600, self.emp.tax)

    def test_bonus(self):

        self.emp.apply_bonus()
        self.assertAlmostEqual(88000, self.emp.salary)




