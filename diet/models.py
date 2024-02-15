from django.db import models
from django.contrib.auth.models import User
import datetime


class DietTag(models.Model):
    tag_name = models.CharField(max_length=32)

    def __str__(self):
        return self.tag_name



class DietPlan(models.Model):
    DIET_TYPES = [
        ('VG', 'Vegetarian'),
        ('VN', 'Vegan'),
        ('MT', 'Meat'),
        ('PS', 'Pescatarian'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(DietTag)
    created_on = models.DateTimeField(auto_now_add=True)
    diet_type = models.CharField(max_length=2, choices=DIET_TYPES, default=1)
    start_time = models.TimeField(default=datetime.time(10, 0))
    note = models.CharField(max_length=10)

    class Meta:
        ordering=('created_on',)

    def __str__(self):
        return f'{self.get_diet_type_display()} diet by {self.owner.username}'


