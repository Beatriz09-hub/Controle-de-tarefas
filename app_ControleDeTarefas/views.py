from django.shortcuts import render
from django.http import HttpResponse

def index(request):
return HttpResponse('<h1>Página Inicial</h1>')

def index(request):
return render(request,'app_ControleDeTarefas/index.html')
