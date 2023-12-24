from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Tenant.models import *
# Create your views here.




def index(request):
    if request.method == 'POST':
       
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('Account:home') 
        else:
            messages.error(request, 'Invalid email or password.')
        return redirect('Account:index')
    else:
        return render(request, 'index.html')
    

def home(request):
    property = Property.objects.all()

    context = {
        'property':property
    }
    return render(request,'home.html', context)
