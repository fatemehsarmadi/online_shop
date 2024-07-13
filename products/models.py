from django.db import models

class AbstractProductModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=1, decimal_places=1)

    class Meta:
        abstract = True