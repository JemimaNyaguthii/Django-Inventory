# forms.py
from django import forms
from .models import Customer

class CustomerUploadForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = []  # Add the fields you want to exclude from the form
        widgets = {
            'field_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        def clean_field_name(self):
            field_name = self.cleaned_data['field_name']
            return field_name
