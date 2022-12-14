from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def query_param(request):
  get_value = request.GET['send_value_to_requestGET']
  return HttpResponse('test query parameter:' + get_value + '左に出てるのがクエリパラメータで受け取った値')

def query_param_smart_version(request, id, name):
  get_value = 'your id : ' + str(id) + 'your name : ' + str(name)
  return HttpResponse(get_value)
  
# request.GETは辞書型になっていて
# アドレスに ?send_value_to_requestGET=******と入力すると
# { 'send_value_to_requestGET':*****}
#という値を格納してれる。
#なので、request.GETにkeyを与えれば値を出力してくれるという仕組み