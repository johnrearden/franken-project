from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    nickname = models.CharField(max_length=50)
    avatar = models.ImageField(
        default='placeholder.png',
        upload_to='images/')

    def __str__(self):
        return self.user.username