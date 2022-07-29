from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates a user with a given email and password
        """
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None):
        """
        Creates and saves a staff user with a given email and password
        """
        if not email:
            raise ValueError("Users must have a valid email address")
        user = self.model(
            email=email,
            is_staff=True
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with a given email and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusers must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Supersusers must have is_superuser=True')
        return self.create_user(email, password, **extra_fields)

