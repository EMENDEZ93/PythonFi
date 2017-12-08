from django.db import models


class ManagerNewMethod(models.Manager):
    def lastname_filter(self,keyword):
        return self.filter(nametest__icontains=keyword).count()

class ModelTest(models.Model):
    nametest = models.CharField(max_length=30)
    objects = ManagerNewMethod()


    def __str__(self):
        return self.nametest
