from django.db import models
from services.models import Service


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)  # For Stripe tracking later

    def __str__(self):
        return f"{self.name} - {self.service.name} on {self.date}"
