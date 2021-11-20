from django.db import models
from django.db.models.fields import DateField

from profile_history.models import User_Profile_History

class Music_Style(models.Model):
    """
    Used to create genres of music to group merchandise into
    """
    class Meta:
        verbose_name_plural = 'Music Styles'

    style = models.CharField(max_length=100)

    def __str__(self):
        return self.style


class Merch(models.Model):
    """
    Store merchandise item
    """
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


class Merch_Rating(models.Model):
    """
    Keeps track of ratings for items
    """
    rated_by = models.ForeignKey(
        User_Profile_History, on_delete=models.DO_NOTHING
    )
    rating = models.DecimalField(max_digits=1, decimal_places=0)
    merchandise_id = models.ForeignKey(
        Merch, on_delete=models.CASCADE
    )
