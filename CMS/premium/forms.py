# premium/forms.py
from django import forms
from .models import PremiumSubscription


class PremiumSubscriptionForm(forms.ModelForm):
    class Meta:
        model = PremiumSubscription
        fields = '__all__'




class CustomForm(forms.Form):
    status = forms.CharField()
    message = forms.CharField()
    subject = forms.CharField()
