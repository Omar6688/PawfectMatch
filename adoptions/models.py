from django.db import models

class AdoptablePet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
