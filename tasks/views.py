from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm

# Create your views here.

# Credit to Learn Python on YT (https://www.youtube.com/watch?v=W3yoB0dA4EA)
# for learning how to incorporate the login_required decorator


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(
        request,
        'tasks/task_list.html',
        {'tasks': tasks, }
    )


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            create_form = form.save(commit=False)
            create_form.user = request.user
            create_form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Task successfully added to existing list!'
            )
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            edit_form = form.save(commit=False)
            edit_form.user = request.user
            edit_form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_delete.html', {'task': task})
