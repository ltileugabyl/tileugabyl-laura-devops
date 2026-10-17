import unittest
from app import banner

class TestApplication(unittest.TestCase):

    def test_application_name(self):
        self.assertIn("DevOps Student Application", banner())

    def test_student_name(self):
        self.assertIn("Laura", banner())

    def test_success_message(self):
        self.assertIn("Application is running successfully!", banner())

if __name__ == "__main__":
    unittest.main()
