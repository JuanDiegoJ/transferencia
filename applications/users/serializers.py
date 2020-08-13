from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(required=True)

    def create(self, validate_data):
        usuario = User.objects.create_user(
            validate_data.get('username'),
            validate_data.get('email'),
            validate_data.get('password'),
            first_name=validate_data.get('first_name'),
            last_name=validate_data.get('last_name'),
        )
        return usuario

    def validate_username(self, data):
        usuario = User.objects.filter(username = data)
        if len(usuario) != 0:
            raise serializers.ValidationError("Este nombre de usuario ya existe, ingrese uno nuevo")
        else:
            return data


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk',)