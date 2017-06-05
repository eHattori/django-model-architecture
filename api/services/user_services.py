from api.domains.user import UserDomain
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.user_serializer import UserSerializer


class UserServices(APIView):

    def get(self, request):
        #TO-DO
        return Response(
            "teste",
            status=status.HTTP_200_OK,
        )

    def post(self, request):

        #TO-DO
        return Response(
            "teste",
            status=status.HTTP_200_OK,
        )

