from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    role_choices = (
        ("V", "Vendedor"),
        ("G", "Gerente"),
    )
    role = models.CharField(max_length=1, choices=role_choices)
