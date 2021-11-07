from django import forms
from .models import Merch


class MerchForm(forms.ModelForm):

    class Meta:
        model = Merch
        fields= '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            print(field)
            print("-----------")
            # if field.BooleanField:
            #     print("I am ehre")
            # field.widget.attrs['class'] = 'stripe-style-input'