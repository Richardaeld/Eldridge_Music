from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import InvoiceLineItem


@receiver(post_save, sender=InvoiceLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order on lineitem create or update
    """
    instance.invoice.update_total()


@receiver(post_delete, sender=InvoiceLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order on lineitem on deleation
    """
    instance.invoice.update_total()