from django.db import models
from django.db.models.fields import TimeField

class Instrument(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name

    def user_friendly_name(self):
        return self.friendly_name

class Lesson(models.Model):
    instrument = models.ForeignKey('Instrument', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    instrument_level = models.DecimalField(max_digits=2, decimal_place=0)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    new_lesson_day = models.DecimalField(max_digits=1, decimal_places=0)
    lesson_start_time = TimeField(auto_now=False, auto_now_add=False)
    lesson_duration = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.ImageField(null=True, blank=True)
    image_url = models.CharField(max_length=1024, null=True, blank=True)


    def __str__(self):
        return self.name