from django.db import models

# Create your models here.

class class1(models.Model):
    buy_date = models.DateField(null=False,blank=False)
    def __str__(self):
        return self.name

