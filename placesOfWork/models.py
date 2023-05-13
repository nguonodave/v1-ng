from django.db import models

class PlacesOfWork(models.Model):
    place = models.CharField(max_length=100, unique=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "PlaceOfWork"
        verbose_name_plural = "PlacesOfWork"
        # ordering = ("-created_date",)

    def __str__(self):
        return self.place
