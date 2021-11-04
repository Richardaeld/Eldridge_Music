from django.db import models
from django.db.models.fields import DateField
from django_countries.fields import CountryField
from profile_history.models import User_Profile_History
from merchandise.models import Merch
from django.conf import settings
import uuid
from django.db.models import Sum


class Invoice(models.Model ):
    # User/General Information
    invoice_number = models.CharField(max_length=52, null=False, blank=False, editable=False)
    user_profile = models.ForeignKey(User_Profile_History, null=True, blank=True, on_delete=models.SET_NULL, related_name='orders')
    name = models.CharField(max_length=75, null=False, blank=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    street_address_billing = models.CharField(max_length=80, null=False, blank=False)
    street_address_shipping = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    state_county = models.CharField(max_length=80, null=True, blank=True)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Select Your Country', null=False, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    delivery_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    invoice_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _create_invoice_number(self):
        """
        Creates order number with UUID that is unique to this Invoice
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates grand total when a new line item is added
        """
        self.invoice_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.invoice_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_total = self.invoice_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_total = 0
        self.grand_total = self.invoice_total + self.delivery_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Sets new save method that ensures order number has been created
        """
        if not self.invoice_number:
            self.invoice_number = self._create_invoice_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number


class InvoiceLineItem(models.Model):
    invoice = models.ForeignKey(Invoice, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    item = models.ForeignKey(Merch, null=False, blank=False, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Sets new save method that ensures lineitem total and update the invoice total
        """
        self.lineitem_total = self.item.price * self.amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.item.sku} on order {self.invoice.invoice_number}'