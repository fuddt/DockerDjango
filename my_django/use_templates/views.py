from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'use_templates/index.html')

def next_step(request):
	params_dict = {
		'title': 'Next Step',
		'msg' : 'テンプレートに変数を埋め込んでみる',
  		'other_page':'next_step_second'
	}
	return render(request, 'use_templates/next_step.html', params_dict)

def next_step_second(request):
    params_dict = {
		'title' : 'あなたが今見ているのはnext_step_second関数が実行された画面',
		'msg'	: '同じhtmlページの変数の値が変わったページです',
		'other_page':'next_step' 
	}
    return render(request, 'use_templates/next_step.html', params_dict)

def use_static(request):
    params_dict = {
		'title' : 'templatesのstatic使いました。',
		'msg'	: 'css記述するのめんどくさかったらBootstrap使ってね。',
		'other_page':'next_step' 
	}
    return render(request, 'use_templates/use_static.html', params_dict)