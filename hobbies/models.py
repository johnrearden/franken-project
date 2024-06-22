from django.db import models
from django.contrib.auth.models import User


class Hobby(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    since = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='hobby_images/')

    def __str__(self):
        return f'{self.name}, {self.owner.username}\'s hobby'
