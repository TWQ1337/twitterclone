from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False
    )