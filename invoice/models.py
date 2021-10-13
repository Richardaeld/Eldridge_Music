from django.db import models
from django.db.models.fields import DateField
from django_countries.fields import CountryField


class Invoice(models.Model ):
    order_number = models.CharField(max_length=52, null=False, blank=False, editable=False)
    # user_profile = models.ForeignKey('userProfile', null=False, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(max_length=75, null=False, blank=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    cost_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    street_address_billing = models.CharField(max_length=80, null=False, blank=False)
    street_address_shipping = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    state_county = models.CharField(max_length=80, null=True, blank=True)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Select Your Country', null=False, blank=False)