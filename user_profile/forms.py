from django.forms import ModelForm
from .models import UserProfile


class CreateUserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nickname', 'avatar',]
