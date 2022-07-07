from django.db import models
from django.contrib.auth.models import User

class TweetModel(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tweets'
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=500)

    class Meta:
        ordering = ('-timestamp',)