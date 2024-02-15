from django.forms import ModelForm, Select
from django import forms
from .models import DietPlan, DietTag
import datetime as dt

HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(9, 18)]

class DietForm(ModelForm):

    class Meta:
        model = DietPlan
        fields = ['diet_type', 'start_time', 'note', 'tags']
        widgets = {
            'start_time': forms.RadioSelect(choices=HOUR_CHOICES),
        }
    
    tags = forms.ModelMultipleChoiceField(
                queryset=DietTag.objects.all(), widget=forms.CheckboxSelectMultiple
            )