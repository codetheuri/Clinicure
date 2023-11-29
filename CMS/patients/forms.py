from django import forms
from patients.models import patients,treatment


class patientForm(forms.ModelForm):
      class Meta:
        model = patients
        fields = "__all__"

class treatmentForm(forms.ModelForm):
    class Meta:
        model= treatment
        fields= "__all__"



