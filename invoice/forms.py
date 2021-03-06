from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = (
            'name', 'email', 'phone', 'street_address_1',
            'street_address_2', 'city', 'state_county',
            'post_code', 'country',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'city': 'City',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'state_county': 'State',
            'post_code': 'Post Code',
        }

        # Crispy forms configration
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
