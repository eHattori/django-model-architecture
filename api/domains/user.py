from api.models.user import User


class UserDomain:

    def insert(self, user):

        user_model = User()
        user_model.first_name = user.first_name
        user_model.last_name = user.last_name

        return user_model.save()

    def get_all_objects(self):
        return User.objects.all()

