from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Logout view
def logout_view(request):
    logout(request)
    return redirect('task_slate_todo:index')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('task_slate_todo:task_dashboard')

    if request.method == 'POST' and 'login' in request.POST:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('task_slate_todo:task_dashboard')

            else:
                error_message = "Invalid Credentials"
                messages.error(request, error_message)

        except Exception as e:
            error_message = "An error occurred: " + str(e)
            messages.error(request, error_message)

    return render(request, 'authentication/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SignUpForm()

    context = {
        'title': 'Sign Up',
        'form': form
    }

    return render(request, 'authentication/signup.html', context)
