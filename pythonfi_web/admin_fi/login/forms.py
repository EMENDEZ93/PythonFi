# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

"""
class AdForm(forms.Form):
    name = forms.CharField(label=_('Nombre'),max_length=100,
                           widget=forms.TextInput(attrs={
                               'required':'',
                                'class':'form-control gui-input',
                               'placeholder':'Ingresa el título.'
                           }))
    mode = forms.ChoiceField(label=_('Modo'), choices=AdsModeTypes.TYPES, widget= forms.Select(attrs={
                                'class':'form-control gui-input'
    }))
    picture = forms.FileField(label=_('Banner publicitario'), required=False, widget=forms.FileInput())
    order = forms.IntegerField(label=_('Orden'), required=True, widget=forms.NumberInput(attrs={
                                'class':'form-control gui-input',
                           }))
    url = forms.CharField(label=_('URL'),max_length=100,required=False,
                           widget=forms.TextInput(attrs={
                                'class':'form-control gui-input',
                               'placeholder':'Ingresa la url.'
                           }))
    target = forms.ChoiceField(label=_('¿Cómo deseas abrir el enlace?'), choices=AdsTargetTypes.TYPES,
                               widget= forms.Select(attrs={
                                'class':'form-control gui-input'
    }))
    code = forms.CharField(label=_('Código HTML'), max_length=1024, required=False,
                           widget=forms.Textarea(attrs={
                                'class':'form-control gui-input',
                           }))


    def __init__(self, website, *args, **kwargs):
        super(AdForm, self).__init__(*args, **kwargs)
        self.website=website

    def save(self, object=None):
        if not object:
            object = Ads(
                name=self.cleaned_data['name'],
                picture=self.cleaned_data['picture'],
                url=self.cleaned_data['url'],
                target=self.cleaned_data['target'],
                mode=self.cleaned_data['mode'],
                code=self.cleaned_data['code'],
                order=self.cleaned_data['order'],
                website=self.website,
            )
            object.save()
        else:
            object.name=self.cleaned_data['name']
            object.picture=self.cleaned_data['picture']
            object.url=self.cleaned_data['url']
            object.target=self.cleaned_data['target']
            object.mode=self.cleaned_data['mode']
            object.code=self.cleaned_data['code']
            object.order=self.cleaned_data['order']
            object.save()
        return object

    """