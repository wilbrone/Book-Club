import unittest
from app.models import User
from app import db

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.new_user= User ( username="Jumpman",
                              full_name="John Doe",
                              email="jumpman@gmail.com",
                              pass_secure="testing12"
                              )
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))
