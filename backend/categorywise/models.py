from django.db import models
from category.models import Category

class Categorywise(models.Model):
    categoryID = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    stock = models.CharField(max_length=255, default='', blank=False, null=True)

    def __str__(self):
        return str(self.categoryID) + " - "+ self.stock