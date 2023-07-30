from django.db import models
from django.utils import timezone


class Property(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    url = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name  # changed from self.code to self.name
