from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    nickname = models.CharField(max_length=6)
    avatar = models.ImageField(
        default='placeholder.png',
        upload_to='images/')
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}, nickname={self.nickname}, avatar={self.avatar.url}' 