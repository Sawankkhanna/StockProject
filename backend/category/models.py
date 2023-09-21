from django.db import models

class Category(models.Model):
    categoryID = models.CharField(max_length=10, default='', blank=False, null=False)
    categoryName = models.CharField(max_length=255, default='', blank=False, null=True)
    totalStocks = models.IntegerField()

    def __str__(self):
        return self.categoryID + " - "+ self.categoryName