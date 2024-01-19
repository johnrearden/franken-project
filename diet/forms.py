from django.forms import ModelForm, Select
from .models import DietPlan
import datetime as dt

HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(9, 18)]

class DietForm(ModelForm):

    class Meta:
        model = DietPlan
        fields = ['diet_type', 'start_time']
        widgets = {
            'start_time': Select(choices=HOUR_CHOICES),
        }