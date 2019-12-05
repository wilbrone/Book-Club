import unittest
from app.models import User, Books
from app import db

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.new_user= User (
                              username="Jumpman",
                              full_name="John Doe",
                              email="jumpman@gmail.com",
                              pass_secure="testing12"
                               )
        self.new_user.save_user()

        self.new_book=Books( title="tester", author="writer", description="big book", user_id=self.new_user.id)
        self.new_book.save_book()

    def test_instances(self):

        self.assertTrue(isinstance(self.new_user, User))
        self.assertTrue(isinstance(self.new_book, Books))

    def test_user_issaved(self):
        self.new_user.save_user()
        self.assertTrue(len(User.query.all())> 0)

    def test_books_issaved(self):
        self.new_book.save_book()
        self.assertTrue(len(Books.query.all())> 0)


class TestPasswords(unittest.TestCase):

    def setUp(self):
        self.new_password = User(pass_secure='testing12')
        self.new_password.save_user()

    def test_password_tester(self):
        self.assertTrue(self.new_password.pass_secure is not None )

    def test_verification(self):
        self.assertTrue(self.new_password.pass_secure, ('testing12') )
