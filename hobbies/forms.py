from django import forms
from .models import Hobby


class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['name', 'description', 'since', 'image']
        widgets={
            'since':forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                
            }),
            'description': forms.Textarea(attrs={
                'cols': 10, 
                'rows': 2,
                'placeholder': 'Describe your hobby',
            }),
            
        }