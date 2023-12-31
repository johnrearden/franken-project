from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'nickname', 'avatar', 'video_clip', 'apology')
    list_editable = ('user', 'nickname', 'avatar', 'video_clip', 'apology')
