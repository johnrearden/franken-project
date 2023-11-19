from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget
from .models import UserProfile


class CreateUserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['nickname', 'avatar', 'video_clip', 'apology']
        widgets = {
            'apology': SummernoteWidget()
        }