from re import L
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .utils.manage import BaseUserManager

ALLOWED_STATUS = [
    ("ACTIVE", "ACTIVE"),
    ("SUSPENDED", "SUSPENDED")
]

ALLOWED_GENDER = [
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE")
]


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class MyUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=ALLOWED_GENDER)
    email = models.EmailField(unique=True, blank=False, null=False)
    admin = models.BooleanField(default=False) # a superuser
    staff = models.BooleanField(default=False) # an admin user; a non superuser 
    status = models.CharField(max_length=255, choices=ALLOWED_STATUS, default="ACTIVE")
    is_phone_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)

    objects = BaseUserManager()
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        """
        Is the user a member of staff?
        """
        return self.staff

    @property
    def is_staff(self):
        """
        Is the user an admin member?
        """
        return self.admin
        