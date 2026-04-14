from django.shortcuts import redirect, render
from app_ControleDeTarefas.models import Tarefa
from django.contrib.auth.decorators import login_required

@login_required 
def tarefas(request):
    banco = Tarefa.objects.all()
    return render(request,'app_ControleDeTarefas/ControleDeTarefas.html', {'banco': banco })
@login_required
def criar(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        status = False
        Tarefa.objects.create(titulo=titulo, descricao=descricao, data=data, status=status)
        return redirect('tarefas')
    return render(request, 'app_ControleDeTarefas/criar.html')
@login_required
def excluir(request,id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefas')
    return render(request, 'app_ControleDeTarefas/excluir.html')
