from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import *
from .models import PokemonInfo
from django.core.paginator import Paginator

# Create your views here.
class GetRecords(TemplateView):
    def __init__(self, num = 1):
        records = PokemonInfo.objects.all()
        self.pagenator = Paginator(records, 2)
        self.params = {
                'form' : GetForm(),
                'records': self.pagenator.get_page(num)
        } 
    def get(self, request, num = 1):
        self.params['records'] = self.pagenator.get_page(num)
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

        
class Find(TemplateView):
    def __init__(self):
        self.params = {
            'records': None,
            'form': FindForm(),
        }
    def get(self, request):
        self.params['records'] = PokemonInfo.objects.all()
        return render(request, 
                      template_name='use_db/find.html',
                      context= self.params)
        
    def post(self, request):
        self.params['form'] = FindForm(request.POST)
        self.params['records'] = (PokemonInfo.objects
                                             .filter(trainers_name__contains=request.POST['find']))
        return render(request, 
                      template_name='use_db/find.html',
                      context= self.params)
        
class MyValidation(TemplateView):
    def __init__(self):
        self.params = {
            'records': None,
            'form': MyValidationForm(),
            'modelforms':PokemonInfoForm(),
        }
    def get(self, request):
        self.params['records'] = PokemonInfo.objects.all()
        return render(request, 
                      template_name='use_db/valid.html',
                      context= self.params)
        
    def post(self, request):
        self.params['form'] = MyValidationForm(request.POST)
        self.params['records'] = (PokemonInfo.objects
                                             .filter(trainers_name__contains=request.POST['find']))
        return render(request, 
                      template_name='use_db/valid.html',
                      context= self.params)