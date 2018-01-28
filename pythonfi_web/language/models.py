from django.db import models
from django.utils.translation import ugettext_lazy as _


class Language(models.Model):
    name = models.CharField(_('Lenguaje de programacion'), max_length=255)
    description = models.TextField(_('Descripción'), null=True, blank=True)