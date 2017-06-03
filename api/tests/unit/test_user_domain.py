from django.test import TestCase
from api.domains.user import UserDomain
import mock
import pytest


import pymysql
pymysql.install_as_MySQLdb()


@pytest.mark.django_db
class UserDomainTest(TestCase):

    def setUp(self):
        self.domain = UserDomain()

    def test_deveria_inserir_um_usuario(self):
        user = mock.Mock()
        user.first_name = "First name"
        user.last_name = "Last name"

        new_user = self.domain.insert(user)
        self.assertEqual(new_user, None)
