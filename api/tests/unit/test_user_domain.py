from django.test import TestCase
from api.domains.user import UserDomain
import mock


class UserDomainTest(TestCase):

    def setUp(self):
        self.domain = UserDomain()

    def test_deveria_inserir_um_usuario(self):
        user = mock.Mock()
        user.first_name = "First name"
        user.last_name = "Last name"

        self.domain.insert(user)
        all_users = self.domain.get_all_objects().first()
        self.assertEqual(all_users.first_name, "First name")
