from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'app_ControleDeTarefas/index.html')

def tarefas(request):
    return render(request,'app_ControleDeTarefas/ControleDeTarefas.html')