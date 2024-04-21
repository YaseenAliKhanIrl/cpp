from django.db import models
from datetime import date
from django.utils.timezone import datetime

class GymSlot(models.Model):
    time = models.TimeField()
    available = models.BooleanField(default=True)

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(default=date.today())  # Changed to DateField
    time = models.TimeField(default=datetime.now())  # Changed to TimeField
    
    def __str__(self):
        return f'{self.name}'
