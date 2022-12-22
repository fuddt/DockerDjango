from django.urls import path , re_path
from .views import *

urlpatterns = [
    path(route='', view=IndexView.as_view(), name='index'),
]
