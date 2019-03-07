from .models import ContactUsModel
from django import forms


class ContactUsForm(forms.ModelForm):
    class Meta:
        model=ContactUsModel
        fields = "__all__"

