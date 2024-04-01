from typing import Any, Dict

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(
        self, email: str, password: str, **kwargs: Dict[str, Any]
    ) -> "User":
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self, email: str, password: str, **kwargs: Dict[str, Any]
    ) -> "User":
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_staff", True)

        return self.create_user(email=email, password=password, **kwargs)


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    hashed_password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return super().__str__() + f" {self.username} {self.email}"
