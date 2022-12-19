from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PokemonInfoForm

# Create your views here.

class PokemonInfoView(TemplateView):
    def __init__(self):
        self.params={
            'form':PokemonInfoForm(),
            'input_informations':"you haven't input your information",
        }
    
    def get(self, request):
        return render(request, 'forms_class/index.html', self.params)
    
    def post(self, request):
        usr_info = 'trainer name :' + request.POST['trainers_name'] +'<br>' +\
            "pokemon's name:" + request.POST['pokemons_name'] + '<br>' +\
            "pokemon's level" + request.POST['pokemons_level'] + '<br>' +\
            "<p>self introduciton:</p>" + request.POST['self_intro']
        self.params['input_informations'] = usr_info
        self.params['form'] = PokemonInfoForm(request.POST)
        return render(request, 'forms_class/index.html', self.params)