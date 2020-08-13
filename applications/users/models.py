from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=30)
    first_name = models.CharField('Nombres', max_length=50, blank=True)
    last_name = models.CharField('Apellidos', max_length=50, blank=True)
    is_staff = models.BooleanField(default=False)
    retirado = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    

    