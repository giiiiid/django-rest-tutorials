from rest_framework.test import APITestCase
from ..models import User

class TestUser(APITestCase):

    def test_user_creation(self):
        user = User.objects.create_user('kofi', 'kofi@gmail.com', 'kofi123')
        self.assertIsInstance(user, User)