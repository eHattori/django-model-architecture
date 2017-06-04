from api.models.user import User


class UserDomain:

    @staticmethod
    def create(user):

        try:
            user_model = User()
            user_model.first_name = user.first_name
            user_model.last_name = user.last_name

            user_model.save()
            return user_model
        except AttributeError as e:
            pass

    @staticmethod
    def get_all_objects():
        return User.objects.all()

    @staticmethod
    def update(user):
        user_model = User.objects.get(id=user.id)

        user_model.first_name = user.first_name
        user_model.last_name = user.last_name

        user_model.save()
        return user_model

    @staticmethod
    def get_user_by_id(id):
        try:
            user_model = User.objects.get(id=id)
            return user_model
        except User.DoesNotExist as e:
            return None

    @staticmethod
    def delete(user):
        User.objects.get(id=user.id).delete()


