from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    selected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
