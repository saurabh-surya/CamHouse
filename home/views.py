from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name =request.POST.get('name')
        email =request.POST.get('email')
        desc =request.POST.get('desc')
        contact=Contact(name=name,email=email,desc=desc)
        contact.save()
    return render(request, 'contact.html')

def brands(request):
    return render(request, 'brands.html')

def nikon(request):
    return render(request, 'nikon.html')