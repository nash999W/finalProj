from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Image(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True, default=None)
    predicted_result = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
