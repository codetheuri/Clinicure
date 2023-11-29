from django.db import models


class staffs(models.Model):
    POSITION_CHOICES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('receptionist', 'Administrator'),
        ('pharmacy', 'Pharmacist')

    ]
    full_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, default='doctor')






    def __str__(self):
        return f"{self.full_name} - {self.position}"

class staffrole(models.Model):
    role_name = models.CharField(max_length=50, unique=True)
    staff= models.ForeignKey(staffs, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.role_name} -{self.staff}"
