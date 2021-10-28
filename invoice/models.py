from django.db import models
from django.db.models.fields import DateField
from django_countries.fields import CountryField
from profile_history.models import User_Profile_History
import uuid


class Invoice(models.Model ):
    # User/General Information
    order_number = models.CharField(max_length=52, null=False, blank=False, editable=False)
    user_profile = models.ForeignKey(User_Profile_History, null=True, blank=True, on_delete=models.SET_NULL, related_name='orders')
    name = models.CharField(max_length=75, null=False, blank=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    # cost_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    street_address_billing = models.CharField(max_length=80, null=False, blank=False)
    street_address_shipping = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    state_county = models.CharField(max_length=80, null=True, blank=True)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Select Your Country', null=False, blank=False)
    # Lesson Information
    sku = models.CharField(max_length=254, null=True, blank=True)
    instrument = models.CharField(max_length=100)
    instrument_level = models.CharField(max_length=50)
    class_type = models.CharField(max_length=11)
    subscription_months = models.CharField(max_length=2)
    lessons_per_week = models.CharField(max_length=1)
    lesson_minutes = models.CharField(max_length=2)
    payment_frequency = models.CharField(max_length=20)
    # price_paid = models.DecimalField(max_digits=7, decimal_places=2)
    price_total = models.DecimalField(max_digits=7, decimal_places=2)

    def _create_order_number(self):
        """
        Creates order number with UUID that is unique to this Invoice
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Sets new save method that ensures order number has been created
        """
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number