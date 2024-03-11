import unittest
from solid import Manager, Developer

class TestManager(unittest.TestCase):
    def setUp(self):
        self.manager = Manager("Alice")

    def test_calculate_bonus(self):
        # Test bonus calculation for a manager
        self.assertEqual(self.manager.calculate_bonus(), 1000)

    def test_manage_team(self):
        # Test the manage_team method
        expected_output = "Alice is managing the team."
        self.assertEqual(self.manager.manage_team(), expected_output)

class TestDeveloper(unittest.TestCase):
    def setUp(self):
        self.developer = Developer("Bob")

    def test_calculate_bonus(self):
        # Test bonus calculation for a developer
        self.assertEqual(self.developer.calculate_bonus(), 500)

    def test_code_review(self):
        # Test the code_review method
        expected_output = "Bob is conducting a code review."
        self.assertEqual(self.developer.code_review(), expected_output)

if __name__ == '__main__':
    unittest.main()
