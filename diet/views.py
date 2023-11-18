from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import DietPlan


class DietList(ListView):
    model = DietPlan


class CreateDiet(CreateView):
    model = DietPlan
    fields = ['diet_type',]
    success_url = reverse_lazy('diet_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)