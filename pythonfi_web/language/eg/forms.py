from django import forms
from pythonfi_web.language.models import Language


class AjaxCrudForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ('name', 'description',)