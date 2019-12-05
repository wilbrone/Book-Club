import unittest
from .models import User
from app import db

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.new_user= User ('Jumpman', 'John Doe', 'jumpman@gmail.com', 'testing12')

    def test_instance(self):
        self.assertTrue()
