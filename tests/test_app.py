import unittest
from app import validate_user


class TestValidateUser(unittest.TestCase):
    def test_valid_user(self):
        self.assertTrue(validate_user("Shalini", 24))

    def test_empty_name_is_invalid(self):
        self.assertFalse(validate_user("", 24))

    def test_underage_user_is_invalid(self):
        self.assertFalse(validate_user("Alex", 16))

    def test_invalid_age_type(self):
        self.assertFalse(validate_user("Alex", " twenty "))


if __name__ == "__main__":
    unittest.main()
