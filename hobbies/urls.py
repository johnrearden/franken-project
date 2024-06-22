from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import HobbyList

urlpatterns = [
    path('', HobbyList.as_view(), name='hobby_list'),
]