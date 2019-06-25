from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Portfolio(models.Model):
    portfolio_name = models.CharField(max_length=150)
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio_label = models.CharField(max_length=100, blank=True, default='')


    def __str__(self):
        return self.portfolio_name

    def get_absolute_url(self):
        return reverse('portfolio-detail', kwargs={'pk': self.pk})



class Position(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    transaction_type = models.CharField(max_length=15)
    shares = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField(null=True)
    commission = models.DecimalField(decimal_places=2, max_digits=6,null=True)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.symbol