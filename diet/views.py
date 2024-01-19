from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from .models import DietPlan
from .forms import DietForm


class DietList(ListView):
    model = DietPlan


class CreateDiet(CreateView):
    model = DietPlan
    form_class = DietForm
    success_url = reverse_lazy('diet_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class UpdateDiet(UpdateView):
    model = DietPlan
    form_class = DietForm
    success_url = reverse_lazy('diet_list')