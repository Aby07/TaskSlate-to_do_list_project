from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def login_view(request):
    if request.POST and 'login' in request.POST:
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                success_message="Login Successful"
                messages.success(request, success_message)

            else:
                error_message = "Invalid Credintials"
                messages.error(request, error_message)

        except Exception as e:
            error_message="An error occured" + str(e)
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


