from django.shortcuts import render
from django.views import View

# Create your views here.

class MapView(View):
    def get(self, request):
        return render(request, 'random_map/map.html')