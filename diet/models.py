from django.db import models
from django.contrib.auth.models import User

class DietPlan(models.Model):

    DIET_TYPES = [
        ('VG', 'Vegetarian'),
        ('VN', 'Vegan'),
        ('MT', 'Meat'),
        ('PS', 'Pescatarian'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    diet_type = models.CharField(max_length=2, choices=DIET_TYPES, default=1)

    def __str__(self):
        return f'{self.get_diet_type_display()} diet by {self.owner.username}'