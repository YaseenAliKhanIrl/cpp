from django.db import models

class GymSlot(models.Model):
    time = models.TimeField()
    available = models.BooleanField(default=True)

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    slot = models.ForeignKey(GymSlot, on_delete=models.CASCADE)
