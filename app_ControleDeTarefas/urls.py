from django.urls import path
from app_ControleDeTarefas.views import index, tarefas

urlpatterns = [
path('', index, name='index'),
path('tarefas/', tarefas, name='tarefas')
]

