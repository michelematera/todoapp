from django.contrib.auth import models as auth_models
from django.db import models

from todoapp.utils import timepiece
from todoapp import abstract_models as am


class User(
    am.TimedatedModel,
    am.IsActiveModel,
    am.AdminChangeUrlModel,
    auth_models.AbstractBaseUser,
    auth_models.PermissionsMixin
):
    USERNAME_FIELD = 'username'
    objects = auth_models.UserManager()

    username = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', default=timepiece.now)
    first_name = models.CharField(verbose_name='first name', max_length=100, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=150, blank=True)
    email = models.EmailField(verbose_name='email')

    def __str__(self):
        return (
            (self.is_staff and self.username)
            or f'{self.first_name} {self.last_name}'.strip()
            or self.email.partition('@')[0] if self.email is not None else 'Unknown'
        )

    class Meta:
        ordering = ['-id']
        verbose_name = 'user'
        verbose_name_plural = 'users'
