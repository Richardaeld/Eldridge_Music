from django.db import models
from django.db.models.fields import TimeField

# ------------------------------------------Many To Many Models
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


# Creates lessons per week
class Lessons_Per_Week(models.Model):
    one_lesson  = '1'
    two_lesson = '2'
    three_lesson = '3'
    LESSONS_PER_WEEK = [
        (one_lesson, '1'),
        (two_lesson, '2'),
        (three_lesson, '3'),
    ]
    weekly_lessons = models.CharField(max_length=1, choices=LESSONS_PER_WEEK, default=one_lesson)

    def __str__(self):
        return self.weekly_lessons


# Creates total length of subscription
class Subscription_Months(models.Model):
    one_month = '1'
    three_months = '3'
    six_months = '6'
    nine_months = '9'
    twelve_months = '12'
    MONTHS_LENGTH = [
        (one_month, '1'),
        (three_months, '3'),
        (six_months, '6'),
        (nine_months, '9'),
        (twelve_months, '12'),
    ]
    months = models.CharField(max_length=2, choices=MONTHS_LENGTH, default=three_months)

    def __str__(self):
        return self.months


# Creates types of lesson offered
class Lesson_Style(models.Model):
    private = 'private'
    group = 'group'
    prerecorded = 'prerecorded'
    LESSONS_TYPE = [
        (private, 'private'),
        (group, 'group'),
        (prerecorded, 'prerecorded'),
    ]
    style = models.CharField(max_length=11, choices=LESSONS_TYPE, default=prerecorded)

    def __str__(self):
        return self.style

# Creates minute length of lessons offered
class Lesson_Minutes(models.Model):
    thirty_minutes = '30'
    forty_five_minutes = '45'
    sixty_minutes = '60'
    TIME_LENGTH = [
        (thirty_minutes, '30'),
        (forty_five_minutes, '45'),
        (sixty_minutes, '60'),
    ]
    minutes = models.CharField(max_length=2, choices=TIME_LENGTH, default=sixty_minutes)

    def __str__(self):
        return self.minutes


# ------------------------------------------Lessons and Subscription Models
# Creates lessons/classes
class Lesson(models.Model):
    instrument = models.ForeignKey('Instrument', null=True, blank=True, on_delete=models.SET_NULL)
    instrument_level = models.ForeignKey('Instrument_level', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    duration = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    image = models.ForeignKey('Image', null=True, blank=True, on_delete=models.SET_NULL)
    class_type = models.ManyToManyField('Lesson_Style')
    subscription_months = models.ManyToManyField('Subscription_Months')
    lessons_per_week = models.ManyToManyField('Lessons_Per_week')
    lesson_minutes = models.ManyToManyField('Lesson_Minutes')

    def __str__(self):
        return self.name


# Creates subscription types
class Subscription(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    instrument = models.ManyToManyField('Instrument')
    instrument_level = models.ManyToManyField('Instrument_Level')
    image = models.ForeignKey('Image', null=True, blank=True, on_delete=models.SET_NULL)
    class_type = models.ManyToManyField('Lesson_Style')
    subscription_months = models.ManyToManyField('Subscription_Months')
    lessons_per_week = models.ManyToManyField('Lessons_Per_week')
    lesson_minutes = models.ManyToManyField('Lesson_Minutes')
    description = models.TextField()
    active_subscription = models.BooleanField(default=True)

    # price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name

    def user_friendly_name(self):
        return self.friendly_name
