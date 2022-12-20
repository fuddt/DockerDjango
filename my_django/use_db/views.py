from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import PokemonInfoForm
from .forms import GetForm
from .models import PokemonInfo

# Create your views here.
class GetRecords(TemplateView):
    def __init__(self):
        self.params = {
                'form' : GetForm(),
                'records': []
        }
    
    def get(self, request):
        self.params['records'] = PokemonInfo.objects.all()
        return render(request, 'use_db/get_records.html', self.params)
    
    def post(self, request):
        target_records = PokemonInfo.objects.get(id=request.POST['id'])
        self.params['records'] = [target_records]
        self.params['form'] = GetForm(request.POST)    
        return render(request, 'use_db/get_records.html', self.params)

class CreateRecords(TemplateView):
    def __init__(self):
        self.params = {
                'input_informations': "you haven't input your information",
                'form': PokemonInfoForm(),
                }
    def get(self, request):
        return render(request, 'use_db/create_records.html', self.params)

    def post(self, request):
        pokemon_info_form = PokemonInfoForm(request.POST, instance=PokemonInfo())
        pokemon_info_form.save()
        return redirect(to='/use_db/create_records')


class UpDateRecords(TemplateView):
    def __init__(self):
        self.params = {
            'message':'You can update records',
        }
    
    #クエリパラメータの処理
    def query_param(self, request, num):
        target_records = PokemonInfo.objects.get(id=num)
        self.params['id'] = num
        self.params['form'] = PokemonInfoForm(instance=target_records)
    
    def get(self, request, num):
        self.query_param(request, num)
        return render(request, 'use_db/update_records.html', self.params)
    
    def post(self, request, num):
        self.query_param(request, num)
        pokemon_info_form = PokemonInfoForm(request.POST, instance= PokemonInfo.objects.get(id=num))
        pokemon_info_form.save()
        return redirect(to='/use_db/get_records')

        
class DeleteRecords(TemplateView):
    def __init__(self):
        self.params = {
            'message':'You can update records',
        }
    #クエリパラメータの処理
    def query_param(self, request, num):
        target_records = PokemonInfo.objects.get(id=num)
        self.params['id'] = num
        self.params['form'] = PokemonInfoForm(instance=target_records)
                
    def get(self, request, num):
        self.query_param(request, num)
        return render(request, 'use_db/delete_records.html', self.params)
    
    def post(self, request, num):
        self.query_param(request, num)
        delete_records = PokemonInfo.objects.get(id=num)
        delete_records.delete()
        return redirect(to='/use_db/get_records')

        
        