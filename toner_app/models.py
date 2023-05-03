from django.db import models

class Toner(models.Model):
    model = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.model