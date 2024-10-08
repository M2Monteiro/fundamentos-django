from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    slug = models.SlugField()
    banner = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name
