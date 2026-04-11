from django.shortcuts import redirect, render
from app_ControleDeTarefas.models import Tarefa

def index(request):
    return render(request,'app_ControleDeTarefas/index.html')

def tarefas(request):
    banco = Tarefa.objects.all()
    return render(request,'app_ControleDeTarefas/ControleDeTarefas.html', {'banco': banco })

def criar(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        status = False
        Tarefa.objects.create(titulo=titulo, descricao=descricao, data=data, status=status)
        return redirect('tarefas')
    return render(request, 'app_ControleDeTarefas/criar.html')

def excluir(request,id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefas')
    return render(request, 'app_ControleDeTarefas/excluir.html')
