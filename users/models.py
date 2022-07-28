from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # an admin user; non-superuser
    admin = models.BooleanField(default=False)  # a superuser

    # notice the absence of the "password field", which is built in

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email and Password are required by default

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

