from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

#@python_2_unicode_compatible
#class User(AbstractUser):
#
#    name = models.CharField(_('Nombre completo'), blank=True, max_length=255)
#
#
#    def __str__(self):
#        return self.username
