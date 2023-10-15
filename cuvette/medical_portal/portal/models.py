# portal/models.py

from django.db import models
from django.contrib.auth.models import User

class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed

class Patient(models.Model):
    name = models.CharField(max_length=255)
    receptionist = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # Add other fields as needed
