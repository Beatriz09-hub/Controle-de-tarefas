from django.urls import path
from nome_do_app.views import index

urlpatterns = [
path(''
, index, name=’index’)
]