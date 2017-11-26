from django.db import models

class ModelTest(models.Model):
    nametest = models.CharField(max_length=30)
