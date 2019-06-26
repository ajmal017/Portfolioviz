from django import forms
from django.forms import TextInput

class SymbolForm(forms.Form):
    symbol = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Symbol...',
            'aria-label': 'Search',
            'aria-describedby': 'basic-addon2',
        }
    ), label='', max_length=15)
    widgets = {'name': TextInput(attrs={'class' : 'form-control', 'placeholder':'Symbol'})}