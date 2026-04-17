from django.urls import path, include
from app_ControleDeTarefas.views import tarefas, criar, excluir, editar


urlpatterns = [
path('', tarefas, name='tarefas'),
path('criar/', criar, name="criar"),
path('excluir/<int:id>', excluir, name="excluir"),
path('accounts/', include('django.contrib.auth.urls')),
path('editar/<int:id>/', editar, name="editar")
]

