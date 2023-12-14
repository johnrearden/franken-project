from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import MapView

urlpatterns = [
    path('', views.MapView.as_view(), name='map'),
]
