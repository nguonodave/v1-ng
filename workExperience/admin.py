from django.contrib import admin
from .models import WorkExperience

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "job_title",
        "place_of_Work",
        "period",
    )  # fields to be displayed at the front page of the table in the database dashboard

admin.site.register(WorkExperience, WorkExperienceAdmin)
