from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    diameter = models.IntegerField(default=25)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='pizza/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('song', kwargs={'pizza_id': self.id})


class Order(models.Model):
    pizza = models.ForeignKey(Pizza, blank=True, null=True, on_delete=models.CASCADE)
    ingredient = models.ManyToManyField(Ingredient, blank=True, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    number_phone = models.CharField(max_length=10)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
