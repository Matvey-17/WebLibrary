from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from Users.api.serializers import RegisterSerializer, LoginSerializer, RegisterLibrianSerializer

from rest_framework import status

from rest_framework.response import Response

from djoser import utils
from djoser.conf import settings


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)


class RegisterLibrianView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterLibrianSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                token = utils.login_user(self.request, user)
                token_serializer_class = settings.SERIALIZERS.token
                response = Response(
                    data=token_serializer_class(token).data, status=status.HTTP_200_OK
                )
                response.set_cookie('token', token_serializer_class(token).data['auth_token'], max_age=604800)
                return response
            else:
                return Response({'detail': ['Пользовтель не найден']}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        utils.logout_user(request)
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('token')
        return response
