from django.contrib import admin
from .models import DietPlan


@admin.register(DietPlan)
class DietPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'created_on', 'diet_type')
    list_editable = ('owner', 'diet_type')
    list_filter = ['diet_type', 'created_on']
    search_fields = ['diet_type',]

        
