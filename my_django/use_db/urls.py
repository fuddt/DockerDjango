
from django.urls import path, re_path
from . import views
from .views import *

urlpatterns = [
    path('get_records/', GetRecords.as_view(), name='get_records'), #PokemonInfoView.as_view()は省略せずに書くと views.PokemonInfoView.as_view()です。
    path('get_records/<int:num>', GetRecords.as_view(), name='get_records'),
    path('create_records', CreateRecords.as_view(), name='create_records'),
    path('update_records/<int:num>', UpDateRecords.as_view(), name='update_records'),
    path('delete_records/<int:num>', DeleteRecords.as_view(), name='delete_records'),
    path('find', Find.as_view(), name='find'),
    path('my_validation', MyValidation.as_view(), name='my_validation'),
]