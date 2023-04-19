from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('total_price', 'pizza', 'ingredient')
        fields = '__all__'
