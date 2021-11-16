from django.db import models
from django.db.models.fields import DateField


class Music_Style(models.Model):

    class Meta:
        verbose_name_plural = 'Music Styles'

    style = models.CharField(max_length=100)

    def __str__(self):
        return self.style


class Merch(models.Model):

    class Meta:
        verbose_name_plural = 'Merchandise'

    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    author = models.CharField(max_length=100, null=True, blank=True)
    style = models.ForeignKey(
        Music_Style, null=True, blank=True, on_delete=models.SET_NULL
    )
    release_date = DateField(auto_now=False, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    active_product = models.BooleanField(default=True)
    stocked = models.BooleanField(default=True)
    rating = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    image = models.ImageField(null=True, blank=True)
    image_url = models.CharField(max_length=1024, null=True, blank=True)
    used = models.BooleanField(default=False)
    special = models.BooleanField(default=False)
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return self.name
