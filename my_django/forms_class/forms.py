from django import forms

class PokemonInfoForm(forms.Form):
    trainers_name = forms.CharField(max_length=8, label='trainers_name')
    pokemons_name = forms.CharField(max_length=6, label='pokemons_name')
    pokemons_level = forms.IntegerField(min_value=0, max_value=100, label='pokemons_level')
    self_intro = forms.CharField(widget=forms.Textarea(), max_length=150)
    
    