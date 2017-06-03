from django.test import TestCase
from api.models.user import User
import os

class UserModelTest(TestCase):
    """This class defines the test suite for the user model"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.user_name = "Eduardo"
        self.user = User()

    def test_model_can_create_a_user(self):
        """Test the user model can create a User"""
        old_count = User.objects.count()
        self.user.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)