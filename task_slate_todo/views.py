from django.shortcuts import redirect, render
from .forms import TaskForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import Task

def index(request):
    context={
        'title': 'Home'
    }
    return render(request, 'index.html', context)

@login_required
def task_dashboard(request):
    user = request.user
    user_tasks_count = Task.objects.filter(user=user).count()
    user_completed_tasks_count = Task.objects.filter(user=user, is_completed=True).count()
    user_pending_tasks_count = Task.objects.filter(user=user, is_completed=False).count()
    context = {
        'title': 'Your Task Dashboard',
        'user_tasks_count': user_tasks_count,
        'user_completed_tasks_count': user_completed_tasks_count,
        'user_pending_tasks_count': user_pending_tasks_count
    }
    print('context', context)
    return render(request, 'task_slate_todo/task_dashboard.html', context)

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

    return render(request, 'task_slate_todo/add_task.html', {
        'form': form,
        'title': 'Create Task'
        })

@login_required
def view_tasks_grids(request):
    user = request.user
    all_tasks = Task.objects.filter(user=user)
    context = {
        'title': 'Your Tasks',
        'tasks': all_tasks
    }

    return render(request, 'task_slate_todo/view_task_grid.html', context)

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Your account details have been updated successfully.")
            return redirect('task_slate_todo:profile')
    else:
        form = UserProfileForm(instance=user)
    
    context = {
        'form': form,
        'user': user   
    }
    
    return render(request, 'task_slate_todo/profile.html', context)


