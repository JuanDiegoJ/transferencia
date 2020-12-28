from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib import auth
from .jwt import GenerarToken
from .models import User


class RegistrarUsuarioAPI(APIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = GenerarToken.generar_token(user)
            print(token)
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
                password = serializer.data['password']
                user = auth.authenticate(username=username, password=password)

                if user is not None:
                    
                    token = GenerarToken.generar_token(user)
                    return Response(token, status= status.HTTP_200_OK)

                else:
                    respuesta = {
                        'ok': False,
                        'detail': 'Ingrese la contraseña bien, baboso'
                    }
                    return Response(
                        respuesta,
                        status= status.HTTP_400_BAD_REQUEST
                    )

            except:
                return Response('Contactese con el administrador', status= status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, format=None):

        user = self.request.user
        if user is not None:
            
            token = GenerarToken.generar_token(user)
            return Response(token, status= status.HTTP_200_OK)

        return Response(data, status= status.HTTP_200_OK)