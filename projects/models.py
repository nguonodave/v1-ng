from django.db import models
# from projectCategories.models import ProjectCategory
from ckeditor_uploader.fields import RichTextUploadingField
import uuid


class Projects(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to="projects", blank=True)
    description = RichTextUploadingField(max_length=200, null=True)
    # category = models.ForeignKey(ProjectCategory, on_delete=models.DO_NOTHING)
    # cat = models.CharField(max_length=100, null=True, blank=True)
    github_link = models.CharField(max_length=200, null=True, blank=True)
    preview_link = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField('Tag') # quotes the model tags model is below this model
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        # ordering = ("created_date",)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
