from django.urls import path, include
from app_ControleDeTarefas.views import tarefas, criar, excluir, editar, register_user


urlpatterns = [
path('', tarefas, name='tarefas'),
path('register/', register_user, name='register'),
path('criar/', criar, name="criar"),
path('excluir/<int:id>', excluir, name="excluir"),
path('accounts/', include('django.contrib.auth.urls')),
path('editar/<int:id>/', editar, name="editar")
]

