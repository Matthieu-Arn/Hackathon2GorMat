from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# User signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Welcome {username}, your account has been created!")
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


# User login
def login_view(request):
    # Get the next page to redirect to after login, or default to 'profile'
    next_page = request.GET.get('next', 'profile')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_page)  # Redirect to the intended page after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'users/login.html', {'next': next_page})



# User logout
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')
    

# User profile
@login_required
def profile_view(request):
    return render(request, 'users/profile.html')
