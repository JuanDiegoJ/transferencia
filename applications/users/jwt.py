from rest_framework_simplejwt.tokens import RefreshToken


class GenerarToken():
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'uid': str(user.id),
            'username': str(user.username),
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }