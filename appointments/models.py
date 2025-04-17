from django.db import models
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()



