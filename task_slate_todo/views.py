from django.shortcuts import redirect, render
from .forms import TaskForm 
from django.contrib.auth.decorators import login_required
from .models import Task

def index(request):
    context={
        'title': 'Home'
    }
    return render(request, 'index.html', context)

@login_required
def task_dashboard(request):
    return render(request, 'task_slate_todo/task_dashboard.html', {'title': 'Dashboard'})

@login_required
def add_task(request):
    if request.method == 'POST':  
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user 
            task.save()  
            return redirect('task_slate_todo:task_dashboard') 
    else:
        form = TaskForm() 

    return render(request, 'task_slate_todo/add_task.html', {'form': form})

@login_required
def view_tasks_grids(request):
    user = request.user
    all_tasks = Task.objects.filter(user=user)
    context = {
        'title': 'All Tasks',
        'tasks': all_tasks
    }

    return render(request, 'task_slate_todo/view_task_grid.html', context)


