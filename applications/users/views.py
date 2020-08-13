from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer
from .jwt import GenerarToken
from .models import User

class RegistrarUsuarioAPI(APIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = GenerarToken.get_tokens_for_user(user)
            return Response(token, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):

    serializer_class = LoginSerializer

    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                username = serializer.data['username']
                user = User.objects.get(username = username)
                token = GenerarToken.get_tokens_for_user(user)
                return Response(token, status= status.HTTP_200_OK)
            except:
                return Response('Las credenciales no son validas', status= status.HTTP_500_INTERNAL_SERVER_ERROR)