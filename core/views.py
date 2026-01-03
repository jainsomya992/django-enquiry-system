from django.shortcuts import render, redirect
from .models import Enquiry

def home(request):
    if request.method == "POST":
        Enquiry.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        return redirect('home')

    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')



