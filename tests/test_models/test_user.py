#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Test """

    User = User()
    User.email = "2617@holbertonschool.com"
    User.password = "root"
    User.first_name = "Cristian"
    User.last_name = "Pinzon"

    def test_User(self):
        """test_user"""
        self.assertTrue(True)

    def test_email(self):
        """test email"""
        self.assertTrue(self.User.email)
        self.assertEqual(self.User.email, "2617@holbertonschool.com")

    def test_password(self):
        """test password"""
        self.assertTrue(self.User.password)
        self.assertEqual(self.User.password, "root")

    def test_first_name(self):
        """test first name"""
        self.assertTrue(self.User.first_name)
        self.assertEqual(self.User.first_name, "Cristian")

    def test_last_name(self):
        """test last name"""
        self.assertTrue(self.User.last_name)
        self.assertEqual(self.User.last_name, "Pinzon")


if __name__ == "__main__":
    unittest.main()
