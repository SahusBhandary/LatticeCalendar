from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager

class User(AbstractUser):
    username = models.CharField(max_length=150)
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # Initialize the User Manager
    objects = UserManager()

    def __str__(self):
        return self.email
