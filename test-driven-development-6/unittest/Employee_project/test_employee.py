import unittest
from main import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.e = Employee('Corey', 'Schafer', 50000)

    def test_email(self):
        self.assertEqual(self.e.email, 'Corey.Schafer@email.com')

    def test_fullname(self):
        self.assertEqual(self.e.full_name, 'Corey Schafer')

    def test_pay(self):
        self.e.apply_raise()
        self.assertEqual(self.e.pay, 52500)