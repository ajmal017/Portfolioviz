from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Portfolio(models.Model):
    portfolio_name = models.CharField(max_length=150)
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio_label = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(max_length=1500, blank=True, default='')

    def __str__(self):
        return self.portfolio_name

    def get_absolute_url(self):
        return reverse('portfolio-detail', kwargs={'pk': self.pk})

class Position(models.Model):
    TRANSACTION_CHOICES = (
        ("BUY", "Buy"),
        ("SELL", "Sell"),
    )
    
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    transaction_type = models.CharField(choices=TRANSACTION_CHOICES, default="BUY", max_length=4)
    shares = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    book_value = models.DecimalField(decimal_places=2, max_digits=15, null=True)
    date = models.DateField(null=True)
    commission = models.DecimalField(decimal_places=2, max_digits=6,null=True)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.symbol