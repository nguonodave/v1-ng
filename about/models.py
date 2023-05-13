from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class About(models.Model):
    name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=250, unique=True)
    short_descr = RichTextUploadingField(null=True)
    main_descr = RichTextUploadingField(null=True)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.title