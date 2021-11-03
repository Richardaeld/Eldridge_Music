from django.contrib import admin
from .models import Invoice, InvoiceLineItem


class InvoiceLineItemAdminInLine(admin.TabularInline):
    inlines = InvoiceLineItem
    readonly_fields = ('lineitem_total',)


class InvoiceAdmin(admin.ModelAdmin):
    inlines = (InvoiceLineItemAdminInLine,)

    readonly_fields = ('invoice_number', 'date', 'delivery_total', 'order_total', 'grand_total',)

    fields = ('invoice_number', 'date', 'name', 'email', 'phone', 'country', 'post_code', 'state_country', 'street_address_billing', 'street_address_shipping', 'city', 'delivery_total', 'invoice_total', 'grand_total',)

    list_display = ('invoice_number', 'date', 'name', 'invoice_total', 'delivery_total', 'grand_total',)

    ordering = ('-date')


admin.site.register(Invoice, InvoiceAdmin)