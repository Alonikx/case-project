from .models import RegModel
from django.forms import ModelForm, HiddenInput, TextInput


class RegForm(ModelForm):
    class Meta:
        model = RegModel
        fields = ['date_time', 'quantity_adult', 'quantity_kids', 'price']
        widgets = {
            "date_time": HiddenInput(attrs={'id': 'dt1'}),
            "quantity_adult": HiddenInput(attrs={'id': 'qt1'}),
            "quantity_kids": HiddenInput(attrs={'id': 'qt2'}),
            "price": HiddenInput(attrs={'id': 'pr1'})
        }
