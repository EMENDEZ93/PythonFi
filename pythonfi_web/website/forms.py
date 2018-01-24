from django import forms
from .models import ModelTest


class ModelTestForm(forms.ModelForm):
    class Meta:
        model = ModelTest
        fields = ['nametest', 'lastnametest', 'city', ]
