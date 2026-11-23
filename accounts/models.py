from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.managers import CustomUserManager

import uuid

# Create your models here.

class CustomUser(AbstractUser):

    username = None
    first_name = None
    last_name = None
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    name = models.CharField(max_length=150)

    email = models.EmailField(
        unique=True,
        blank=False
    )

    phone = models.CharField(
        max_length=20
    )

    bio = models.TextField()

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name", "phone"]

    objects = CustomUserManager()

    class Meta:
        ordering = ["email"]

    def __str__(self):
        return self.email