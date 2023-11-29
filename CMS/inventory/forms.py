from django import forms
from inventory.models import item

class itemForm(forms.ModelForm):
       class Meta:
           model = item
           fields= '__all__'
