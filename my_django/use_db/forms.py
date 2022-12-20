from django import forms
from .models import PokemonInfo

class PokemonInfoForm(forms.ModelForm):
    class Meta():
        model = PokemonInfo  
        fields ='__all__'

class GetForm(forms.Form):
    id = forms.IntegerField(label = 'ID')
    