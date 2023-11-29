from django import forms
from staff.models import staffs

class staffForm(forms.ModelForm):
    class Meta:
        model = staffs
        fields = "__all__"