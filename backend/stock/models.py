from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10, default='', blank=False, null=True)
    name = models.CharField(max_length=255, default='', blank=False, null=True)
    marketCap = models.DecimalField(max_digits=255, decimal_places=5, default=0, null=True)
    exchange = models.CharField(max_length=10, default='', blank=False, null=True)
    preMarketChangePercent = models.DecimalField(max_digits=255, decimal_places=5, default=0, null=True)
    postMarketChangePercent = models.DecimalField(max_digits=255, decimal_places=5, default=0, null=True)
    regularMarketPrice = models.DecimalField(max_digits=255, decimal_places=5, default=0, null=True)
    regularMarketChangePercent = models.DecimalField(max_digits=255, decimal_places=5, default=0, null=True)

    def __str__(self):
        return self.symbol + " - "+ self.name