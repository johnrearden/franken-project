from . import views
from django.urls import path
from .views import CreateUserProfileView

urlpatterns = [
    path('create_user_profile',
         views.CreateUserProfileView.as_view(),
         name='create_user_profile'),
]
