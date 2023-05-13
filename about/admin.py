from django.contrib import admin
from .models import About

class AboutAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "title",
    )  # fields to be displayed at the front page of the table in the database dashboard

admin.site.register(About, AboutAdmin)
