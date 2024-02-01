from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = UserProfile
        fields = ['owner', 'nickname', 'avatar', 'video_clip',
                  'apology', 'created_on']