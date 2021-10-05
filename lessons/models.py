from django.db import models
from django.db.models.fields import TimeField


# Creats sharable Images
class Image(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField()
    image_url = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

# Creates instrument difficulty levels
class Instrument_Level(models.Model):
    level = models.CharField(max_length=254)

    def __str__(self):
        return self.level


# Creates instruments
class Instrument(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


# Creates lessons/classes
class Lesson(models.Model):
    instrument = models.ForeignKey('Instrument', null=True, blank=True, on_delete=models.SET_NULL)
    instrument_level = models.ForeignKey('Instrument_level', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    duration = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.ForeignKey('Image', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


# Creates subscription types
class Subscription(models.Model):
    one_lesson  = '1'
    two_lesson = '2'
    three_lesson = '3'
    SUB_LESSONS_PER_WEEK = [
        (one_lesson, '1'),
        (two_lesson, '2'),
        (three_lesson, '3'),
    ]

    three_months = '3'
    six_months = '6'
    nine_months = '9'
    twelve_months = '12'
    SUB_MONTHS_LENGTH = [
        (three_months, '3'),
        (six_months, '6'),
        (nine_months, '9'),
        (twelve_months, '12'),
    ]

    private = 'private'
    group = 'group'
    prerecorded = 'prerecorded'
    SUB_LESSONS_TYPE = [
        (private, 'private'),
        (group, 'group'),
        (prerecorded, 'prerecorded'),
    ]

    thirty_minutes = '30'
    forty_five_minutes = '45'
    sixty_minutes = '60'
    SUB_TIME_LENGTH = [
        (thirty_minutes, '30'),
        (forty_five_minutes, '45'),
        (sixty_minutes, '60'),
    ]

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    instrument_included = models.ManyToManyField('Instrument')
    level_included = models.ManyToManyField('Instrument_Level')
    image = models.ForeignKey('Image', null=True, blank=True, on_delete=models.SET_NULL)
    lesson_class_type = models.CharField(max_length=11, choices=SUB_LESSONS_TYPE, default=prerecorded)
    subscription_duration_months = models.CharField(max_length=2, choices=SUB_MONTHS_LENGTH, default=twelve_months)
    lessons_per_week = models.CharField(max_length=1, choices=SUB_LESSONS_PER_WEEK, default=one_lesson)
    lesson_minutes_length = models.CharField(max_length=2, choices=SUB_TIME_LENGTH, default=sixty_minutes)
    description = models.TextField()
    active_subscription = models.BooleanField(default=True)

    # price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

    def user_friendly_name(self):
        return self.friendly_name


