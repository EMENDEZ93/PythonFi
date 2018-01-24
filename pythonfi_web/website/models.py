from __future__ import unicode_literals
from django.db import models


class ModelTest(models.Model):
    nametest = models.CharField(max_length=30, )
    lastnametest = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nametest


    def id_record(self):
        return self.id

    #class Meta:
