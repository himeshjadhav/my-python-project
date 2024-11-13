from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  # Add logout here
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm, ContactForm
from django.contrib.auth.decorators import login_required

# Signup View
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('contact')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Contact View
@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)  # Logs the user out
    return redirect('login')  # Redirects to the login page after logout
