from django.db import models

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
