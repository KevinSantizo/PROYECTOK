from django.contrib import admin
from tows.models import Crane, Pilot, Assignment
# Register your models here.


@admin.register(Crane)
class CraneAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'trademark', 'year', 'characteristic')


@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'DPI')


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('status', 'pilot_assigned', 'crane_assigned', 'start_time')
