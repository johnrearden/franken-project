from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import UserProfileView

urlpatterns = [
    path('user_profile',
         login_required(views.UserProfileView.as_view()),
         name='user_profile'),
    path('api/user_profile',
          views.UserProfileAPIView.as_view(),
          name='user_profile_api')
]
