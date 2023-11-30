from django.db import models
from staff.models import staffs
from django.contrib.auth.models import User


class patients(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    date_added = models.DateField(auto_now=True)
    staffs = models.ForeignKey(staffs, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class treatment(models.Model):
    date_treated = models.DateField(auto_now=True)
    patient_name = models.ForeignKey(patients, on_delete=models.CASCADE, null=True)
    symptoms = models.TextField(blank=True, null=True)
    conclusion = models.TextField()
    medication = models.TextField()
    cost = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient_name} treated on {self.date_treated}"
