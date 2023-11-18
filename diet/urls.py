from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import DietList, CreateDiet

urlpatterns = [
    path('diet_list', views.DietList.as_view(), name="diet_list"),
    path(
        'create_diet',
        login_required(views.CreateDiet.as_view()),
        name="create_diet"),
]