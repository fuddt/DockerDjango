from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def query_param(request):
  get_value = request.GET['send_value']
  return HttpResponse('GET parameter:' + get_value + ' 受け取った値')

def query_param_smart_version(request, id, name):
  get_value = 'your id : ' + str(id) + 'your name : ' + str(name)
  return HttpResponse(get_value)
  
# request.GETは辞書型になっていて
# アドレスに ?send_value=******と入力すると
# { 'send_value':*****}
#という値を格納してれる。
#なので、request.GETにkeyを与えれば値を出力してくれるという仕組み