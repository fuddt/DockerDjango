from .views import PokemonInfoView
from django.urls import path, re_path


urlpatterns = [
    path('', PokemonInfoView.as_view(), name='index')
]
