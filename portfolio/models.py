from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    mobile_no = models.IntegerField()
    portfolio_value = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=120)
    qty = models.IntegerField()
    company = models.CharField(max_length=120)
    purchase_val = models.FloatField()
    current_val = models.FloatField()

    def __str__(self):
        return self.name

    

