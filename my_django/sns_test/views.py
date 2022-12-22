from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import *
from .models import * 
from django.views.generic import TemplateView
from django.core.paginator import Paginator
# Create your views here.

class IndexView(TemplateView):
    def __init__(self):
        self.params = {
            'title':'Message Board',
            'data': AllMessage.objects.all(),
            'form': MessageForm(),
        }
    def get(self, request):
        return render(request, template_name='sns_test/index.html', context= self.params)
    def post(self, request):
        form_class =MessageForm(request.POST, instance=AllMessage())
        form_class.save()
        return redirect(to='/sns_test')