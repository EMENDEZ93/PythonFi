from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Language(models.Model):
    name = models.CharField(_('Lenguaje de programacion'), max_length=255)
    description = models.TextField(_('Descripción'), null=True, blank=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
