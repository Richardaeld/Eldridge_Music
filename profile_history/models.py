from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_save

class User_Profile_History(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # default_full_name = models.CharField(max_length=75, null=True, blank=True)
    # default_prefered_name = models.CharField(max_length=50, null=True, blank=True)
    # default_pronouns = models.CharField(max_length=10, null=True, blank=True)
    # default_email = models.EmailField(max_length=254, blank=True, null=True)
    default_phone = models.CharField(max_length=20, null=True, blank=True)
    default_street_address_billing = models.CharField(max_length=80, null=True, blank=True)
    default_street_address_shipping = models.CharField(max_length=80, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_state_county = models.CharField(max_length=80, null=True, blank=True)
    default_post_code = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        User_Profile_History.objects.create(user=instance)
    instance.user_profile_history.save()