from django.contrib import admin
from .models import DietPlan, DietTag


@admin.register(DietPlan)
class DietPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'created_on', 'diet_type')
    list_editable = ('owner', 'diet_type')

admin.site.register(DietTag)
