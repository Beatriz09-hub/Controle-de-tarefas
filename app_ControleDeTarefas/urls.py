from django.urls import path, include
from app_ControleDeTarefas.views import tarefas, criar, excluir


urlpatterns = [
path('', tarefas, name='index'),
path('criar/', criar, name="criar"),
path('excluir/<int:id>', excluir, name="excluir"),
path('accounts/', include('django.contrib.auth.urls')),
]

