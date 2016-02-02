import unittest

from app.server import User


class UserModelTestCase(unittest.TestCase):
    '''class to test user creation and
    password verification
    '''

    def test_create_user(self):
        user = User()
        self.assertTrue(user is not None)

    def test_set_password(self):
        user = User(password='123')
        self.assertTrue(user.hashed_pass is not None)

    def test_get_password(self):
        user = User(password='123')
        with self.assertRaises(AttributeError):
            user.password

    def test_verify_password(self):
        user = User(password='123')
        self.assertTrue(user.verify_password('123'))
        self.assertFalse(user.verify_password('321'))
