from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('next_step', views.next_step, name='next_step'),
    path('next_step_second', views.next_step_second, name='next_step_second'),
    path('use_static', views.use_static, name='use_static'),
]
