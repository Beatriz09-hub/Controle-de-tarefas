from django.urls import path
from app_ControleDeTarefas.views import index

urlpatterns = [
path('', index, name='index')
]