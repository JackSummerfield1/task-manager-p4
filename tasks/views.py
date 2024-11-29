from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.

# Credit to Learn Python on YT (https://www.youtube.com/watch?v=W3yoB0dA4EA)
# for learning how to incorporate the login_required decorator


@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(
        request,
        'tasks/task_list.html',
        {
            'tasks': tasks,
        }
    )
