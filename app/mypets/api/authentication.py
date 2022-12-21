from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from mypets.api.serializer import UserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class Login(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh_token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesión Exitoso'
                }, status=status.HTTP_200_OK
                )

        return Response({'error': 'Contraseña o nombre de usuario incorrecto'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', '')).first()
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión Cerrada'}, status=status.HTTP_200_OK)
        return Response({"message": 'El usuario no existe'}, status=status.HTTP_400_BAD_REQUEST)
