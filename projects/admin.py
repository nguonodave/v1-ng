from django.contrib import admin
from .models import Projects, Tag

class ProjectsAdmin(admin.ModelAdmin):
    list_display = (        
        "title",
        # "category",
        "created_date",
        "modified_date",
    )  # fields to be displayed at the front page of the table in the database dashboard

class TagAdmin(admin.ModelAdmin):
    list_display = (        
        "name",
        "created_date",
    )

admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Tag, TagAdmin)
