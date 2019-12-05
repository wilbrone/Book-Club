import unittest
from app.models import User, Books
from app import db

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.new_user= User ( username="Jumpman",
                              full_name="John Doe",
                              email="jumpman@gmail.com",
                              pass_secure="testing12" )

        self.new_book=Books( title="tester", author="writer", description="big book", user_id=self.new_user.id)

    def test_instances(self):
        self.assertTrue(isinstance(self.new_user, User))
        self.assertTrue(isinstance(self.new_book, Books))

    def test_instance_issaved(self):

        self.new_user.save_user()
        self.new_book.save_book()

        self.assertTrue(len(Books.query.all())>0)
        self.assertTrue(len(User.query.all())>0)
