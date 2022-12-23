from django.urls import path 
from . import views

urlpatterns = [
    path('', views.query_param , name='query_param'),
    path('<int:id>/<str:name>/', views.query_param_smart_version,
          name='query_param_smart_version'),
]
