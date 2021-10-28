from django.db import models
from django.db.models.fields import DateField


class Image(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField()
    image_url = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class Music_Style(models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.style


class Merch(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ForeignKey('Image', null=True, blank=True, on_delete=models.SET_NULL)
    author = models.CharField(max_length=100, null=True, blank=True)
    release_date = DateField(auto_now=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    active_product = models.BooleanField(default=True)
    stocked = models.BooleanField(default=True)


    def __str__(self):
        return self.name