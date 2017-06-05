from api.domains.user import UserDomain
from rest_framework import viewsets
from api.serializers.user_serializer import UserSerializer


class UserServices(viewsets.ModelViewSet):
    queryset = UserDomain.get_all_objects()
    serializer_class = UserSerializer
