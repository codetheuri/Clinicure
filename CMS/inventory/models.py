from django.db import models
CATEGORY_CHOICES = [
        ('MEDICINES', 'MEDICINES'),
        ('MEDICAL SUPPLIES', 'MEDICAL SUPPLIES'),
          ]

class item(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='MEDICINES')
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name