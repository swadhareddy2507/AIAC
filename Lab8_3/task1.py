import re
import unittest

def is_valid_email(email):
    """
    Validates an email address using a regular expression.
    Returns True if valid, False otherwise.
    """
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, email))


class TestIsValidEmail(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            "user@example.com",
            "user.name+tag+sorting@example.com",
            "user_name@example.co.uk",
            "user-name@sub.example.org",
            "user123@domain123.com",
            "user@localhost.com",
            "u@e.co"
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_invalid_emails(self):
        invalid_emails = [
            "plainaddress",
            "@missingusername.com",
            "username@.com",
            "username@com",
            "username@domain..com",
            "username@domain.c",
            "username@domain,com",
            "username@domain@domain.com",
            "username@domain .com",
            "username@.domain.com",
            "username@domain.com.",
            "username@-domain.com",
            "username@domain-.com",
            "user name@domain.com",
            "user@domain..com"
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))


if __name__ == "__main__":
    unittest.main()