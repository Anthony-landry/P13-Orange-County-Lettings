from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    r"""Le profile des utilisateurs."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiles")
    r"""L'utilisateur (``OneToOneField``)"""

    favorite_city = models.CharField(max_length=64, blank=True)
    r"""La ville préférée. Maximum 64 caractères (``CharField``)"""

    def __str__(self):
        return self.user.username
