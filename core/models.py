from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.URLField(blank=True)  # For simplicity, using URL-based images

    def __str__(self):
        return self.name
