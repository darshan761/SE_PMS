from django.db import models

# Create your models here.
class User(models.Model):
    Id = models.IntegerField()
    name = models.CharField(max_length=120)
    portfolio_value = models.FloatField()

class Stock(models.Model):
    name = models.CharField(max_length=120)
    qty = models.IntegerField()
    company = models.CharField(max_length=120)
    purchase_val = models.FloatField()
    current_val = models.FloatField()

    

