from django import forms
from .models import Merch, Merch_Rating
from .widgets import CustomClearableFileInput


class MerchForm(forms.ModelForm):

    class Meta:
        model = Merch
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RatingForm(forms.ModelForm):

    class Meta:
        model = Merch_Rating
        fields = '__all__'
