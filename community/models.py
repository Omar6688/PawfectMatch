from django.db import models


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    availability = models.CharField(max_length=200)
    interests = models.TextField(help_text="E.g. Events, Fostering, Transport")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    message = models.TextField(blank=True)
    donated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - £{self.amount}"
