from django.urls import path
from . import views

urlpatterns = [
    path('before_form', views.before_form , name='before_form'),
    path('after_form', views.after_form, name='after_form')
]
