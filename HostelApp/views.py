from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate

# Register view to handle user registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log in the user after registration
            return redirect('index')  # Redirect to homepage after successful registration
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
def index(request):
    return render(request, 'index.html')
def landlord(request):
    return render(request,'landlord-dashboard.html')
def students(request):
    return render(request, 'student-dashboard.html')
def hostel(request):
    return render(request, 'hostel-details.html')