from django.contrib import admin
from .models import PlacesOfWork

class PlacesOfWorkAdmin(admin.ModelAdmin):
    list_display = (
        "place",
    )  # fields to be displayed at the front page of the table in the database dashboard

admin.site.register(PlacesOfWork, PlacesOfWorkAdmin)
