#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Test """

    def test_User(self):
        """test_user"""
        self.assertTrue(True)

    def test_email(self):
        """test email"""
        obj = User()
        obj.email = "holbie@holbertonschool.com"
        self.assertTrue(obj.email)
        self.assertEqual(obj.email, "holbie@holbertonschool.com")

    def test_password(self):
        """test password"""
        obj = User()
        obj.password = "root"
        self.assertTrue(obj.password)
        self.assertEqual(obj.password, "root")

    def test_first_name(self):
        """test first name"""
        obj = User()
        obj.first_name = "Julien"
        self.assertTrue(obj.first_name)
        self.assertEqual(obj.first_name, "Julien")

    def test_last_name(self):
        """test last name"""
        obj = User()
        obj.last_name = "Barbier"
        self.assertTrue(obj.last_name)
        self.assertEqual(obj.last_name, "Barbier")

if __name__ == "__main__":
    unittest.main()
