import unittest

from pages.sign_in_page import SignInPage
from browser import Browser


class Test(unittest.TestCase):
    sign_in_page = None

    def setUp(self):
        self.sign_in_page = SignInPage()
        self.sign_in_page.navigate_to_sign_in_page()

    def tearDown(self):
        self.sign_in_page.close()

    def test_sign_in(self):
        self.sign_in_page.login_user('a@yahoo.com', 'b')

