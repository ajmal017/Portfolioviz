from django import forms
from . models import Position, Portfolio
from django.forms import TextInput,  ModelForm

class AddPositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['portfolio', 'symbol', 'transaction_type', 'shares', 'price', 'date', 'commission', 'date']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AddPositionForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['portfolio'].queryset = Portfolio.objects.filter(user=user) 
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
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

