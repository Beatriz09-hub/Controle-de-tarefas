from django.urls import path
from app_ControleDeTarefas.views import index, tarefas, criar, excluir

urlpatterns = [
path('', index, name='index'),
path('tarefas/', tarefas, name='tarefas'),
path('criar/', criar, name="criar"),
path('excluir/<int:id>', excluir, name="excluir")
]

