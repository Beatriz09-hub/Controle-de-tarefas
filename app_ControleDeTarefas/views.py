from django.shortcuts import  get_object_or_404, redirect, render
from app_ControleDeTarefas.forms import TarefaForm
from app_ControleDeTarefas.models import Tarefa
from django.contrib.auth.decorators import login_required

@login_required 
def tarefas(request):
    banco = Tarefa.objects.filter(usuario = request.user)
    return render(request,'app_ControleDeTarefas/ControleDeTarefas.html', {'banco': banco })
@login_required
def criar(request):
    form = TarefaForm(request.POST or None)
    if request.method == 'POST'and form.is_valid:
        tarefa = form.save(commit = False)
        tarefa.usuario = request.user
        tarefa.save()      
        return redirect('tarefas')
    return render(request, 'app_ControleDeTarefas/criar.html', {'form' : form})
@login_required
def excluir(request,id):
    # tarefa = Tarefa.objects.get(id=id)
    tarefa = get_object_or_404(Tarefa, id=id, usuario = request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefas')
    return render(request, 'app_ControleDeTarefas/excluir.html')

def editar(request, id):

    # tarefa = Tarefa.objects.get(id=id)
    tarefa = get_object_or_404(Tarefa, id=id, usuario = request.user)
    form = TarefaForm(request.POST or None, instance=tarefa)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('tarefas')
    return render(request, 'app_ControleDeTarefas/editar.html', {'form': form, 'tarefa': tarefa})