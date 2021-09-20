from django.db import models
from django.db.models.fields import TimeField


class Instrument_Level(models.Model):
    level = models.CharField(max_length=254)

    def __str__(self):
        return self.level


class Instrument(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    instrument = models.ForeignKey('Instrument', null=True, blank=True, on_delete=models.SET_NULL)
    instrument_level = models.ForeignKey('Instrument_level', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    duration = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.ImageField(null=True, blank=True)
    image_url = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    instrument_included = models.ManyToManyField('Instrument')
    level_included = models.ManyToManyField('Instrument_Level')
    lessons_per_week = models.DecimalField(max_digits=3, decimal_places=0)
    duration_subscription_months = models.DecimalField(max_digits=2, decimal_places=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

    def user_friendly_name(self):
        return self.friendly_name
