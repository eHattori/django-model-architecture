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

        user = self.domain.create(user)

        self.assertNotEqual(user.id, None)

    def test_deveria_falhar_ao_inserir_usuario_invalido(self):
        try:
            self.domain.create("Invalid test")
            self.fail("Insert wrong test")
        except Exception as e:
            pass


    def test_deveria_buscar_todos_usuarios(self):
        user = mock.Mock()
        user.first_name = "First name"
        user.last_name = "Last name"

        self.domain.create(user)

        all_users = self.domain.get_all_objects()
        self.assertNotEqual(len(all_users), 0)

    def test_deveria_atualizar_um_usuario(self):
        user = mock.Mock()
        user.first_name = "First name"
        user.last_name = "Last name"

        user = self.domain.create(user)
        user.first_name = "Other name"
        self.domain.update(user)

        user = self.domain.get_user_by_id(user.id)

        self.assertEquals(user.first_name, "Other name")

    def test_deveria_deletar_usuario(self):
        user = mock.Mock()
        user.first_name = "First name"
        user.last_name = "Last name"

        user = self.domain.create(user)

        self.domain.delete(user)

        not_user = self.domain.get_user_by_id(user.id)
        self.assertEquals(not_user, None)




