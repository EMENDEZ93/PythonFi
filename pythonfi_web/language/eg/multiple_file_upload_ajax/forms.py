from django import forms
from pythonfi_web.language.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file', )
