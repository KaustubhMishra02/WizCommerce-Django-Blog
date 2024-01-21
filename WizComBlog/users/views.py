from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = SignUpForm()
    form = SignUpForm()
    context = {
        'form':form
    }
    return render(request,'users/signup.html',context)

def logoutuser(request):
    logout(request)
    return render(request,'users/logout.html')

def profile(request):
    return render(request,'users/profile.html')