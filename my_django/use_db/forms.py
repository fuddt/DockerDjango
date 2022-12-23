from django import forms
from .models import PokemonInfo
from django.core.exceptions import ValidationError
import re

class PokemonInfoForm(forms.ModelForm):
    class Meta():
        model = PokemonInfo  
        fields ='__all__'

class GetForm(forms.Form):
    id = forms.IntegerField(label = 'ID')

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'})
                            )
    

def contain_numbers(value):
    if (re.search(r'[0-9]', value)):
        raise ValidationError(
            '%s contains numbers you can only strings' % value
        )
        
    
    
class MyValidationForm(forms.Form):
    find = forms.CharField(label='Find', required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}),
                            validators=[contain_numbers]
                            )
    
