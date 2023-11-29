# premium/models.py
from django.db import models
from patients.models import patients


class PremiumSubscription(models.Model):
    patient_status = [
        ('subscribed', 'subscribed'),
        ('unsubscribed', 'unsubscribed')
    ]
    patient = models.ForeignKey(patients, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=patient_status, default='subscribed')
    age= models.IntegerField
    def __str__(self):
        return f'Premium Subscription for {self.patient} '


