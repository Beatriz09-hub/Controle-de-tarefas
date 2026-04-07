from django.urls import path
from app_ControleDeTarefas.views import index, tarefas, criar

urlpatterns = [
path('', index, name='index'),
path('tarefas/', tarefas, name='tarefas'),
path('criar/', criar, name="criar")
]

