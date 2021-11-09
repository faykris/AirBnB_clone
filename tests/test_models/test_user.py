#!/usr/bin/python3

import unittest
from datetime import datetime

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
        self.assertIs(type(self.User.email), str)
        self.assertEqual(self.User.email, "2617@holbertonschool.com")

    def test_password(self):
        """test password"""
        self.assertTrue(self.User.password)
        self.assertIs(type(self.User.password), str)
        self.assertEqual(self.User.password, "root")

    def test_first_name(self):
        """test first name"""
        self.assertTrue(self.User.first_name)
        self.assertIs(type(self.User.first_name), str)
        self.assertEqual(self.User.first_name, "Cristian")

    def test_last_name(self):
        """test last name"""
        self.assertTrue(self.User.last_name)
        self.assertIs(type(self.User.last_name), str)
        self.assertEqual(self.User.last_name, "Pinzon")

    def test_attr_types(self):
        """test id, created and update types"""
        self.assertIs(type(self.User.id), str)
        self.assertIs(type(self.User.created_at), datetime)
        self.assertIs(type(self.User.updated_at), datetime)


if __name__ == "__main__":
    unittest.main()
