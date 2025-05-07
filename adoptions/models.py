from django.db import models

class AdoptablePet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pets/', blank=True, null=True)  # ⬅️ This handles uploads

    def __str__(self):
        return self.name
