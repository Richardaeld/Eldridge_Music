from django.contrib import admin
from .models import Invoice, InvoiceLineItem


class InvoiceLineItemAdminInLine(admin.TabularInline):
    model = InvoiceLineItem
    readonly_fields = ('lineitem_total',)


class InvoiceAdmin(admin.ModelAdmin):
    inlines = (InvoiceLineItemAdminInLine,)

    readonly_fields = ('invoice_number', 'date_time', 'delivery_total',
                        'invoice_total', 'grand_total', 'original_cart',
                        'stripe_pid',)

    fields = ('invoice_number', 'user_profile', 'date_time', 'name', 'email', 'phone',
            'country', 'post_code', 'state_county', 'street_address_billing',
            'street_address_shipping', 'city', 'delivery_total',
            'invoice_total', 'grand_total', 'original_cart', 'stripe_pid',)

    list_display = ('invoice_number', 'date_time', 'name', 'invoice_total',
                    'delivery_total', 'grand_total',)

    ordering = ('-date_time',)


admin.site.register(Invoice, InvoiceAdmin)