from django.shortcuts import render, redirect, get_object_or_404

from .form import TaskForm
from .models import Task


# Create your views here.
def task_list(request):
    task = Task.objects.all()
    return render(request, 'task_lists.html', {'tasks': task})


def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'task_details.html', {'tasks': task})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm
    return render(request, 'task_form.html', {'form': form})


def task_edit(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm(instance=task)
        return render(request, 'task_form.html', {'form': form})


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('')
    return render(request, 'task_confirm_delete.html')
