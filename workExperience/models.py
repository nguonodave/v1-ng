from django.db import models
from placesOfWork.models import PlacesOfWork
from ckeditor_uploader.fields import RichTextUploadingField

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=50)
    place_of_Work = models.ForeignKey(PlacesOfWork, on_delete=models.DO_NOTHING)
    place_of_Work_link = models.CharField(max_length=250, null=True)
    tasks = RichTextUploadingField(null=True)
    period = models.TextField(max_length=50, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "WorkExperience"
        verbose_name_plural = "WorkExperiences"
        # ordering = ("created_date",)

    def __str__(self):
        return self.job_title
