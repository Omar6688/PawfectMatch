from django.db import models


class AdoptablePet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='adoptable_pets/', blank=True, null=True)

    def __str__(self):
        return self.name


class AdoptionInterest(models.Model):
    pet = models.ForeignKey(AdoptablePet, on_delete=models.CASCADE, related_name='interests')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - Interest in {self.pet.name}"
