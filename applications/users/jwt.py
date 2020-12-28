import jwt
from datetime import datetime, timedelta
from django.conf import settings

JWT_EXP_DELTA_SECONDS = 300

class GenerarToken():

    def generar_token(user):

        token = jwt.encode({'username': user.username, 'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)}, settings.JWT_SECRET_KEY, algorithm='HS256')

        data = {
                'username': user.username,
                'uid': user.id,
                'token': token.decode("utf-8"),
                'ok': True
        }

        return data