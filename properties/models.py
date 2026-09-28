from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.PositiveIntegerField()
    surface = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="properties/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title