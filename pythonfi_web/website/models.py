from django.db import models

class ModelTest(models.Model):
    nametest = models.CharField(max_length=30)
    testQuery = models.Manager()


    def __str__(self):
        return self.nametest
