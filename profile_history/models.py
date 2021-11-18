from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class User_Profile_History(models.Model):
    """
    User profile used for remembering default
    shipping information and invoice history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone = models.CharField(max_length=20, null=True, blank=True)
    default_street_address_1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_street_address_2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_state_county = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_post_code = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country *', null=True, blank=True
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates/updates use profiles
    """
    if created:
        User_Profile_History.objects.create(user=instance)
    instance.user_profile_history.save()
