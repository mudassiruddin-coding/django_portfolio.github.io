from django.shortcuts import render, HttpResponse
from datetime import datetime
from port.models import Contact


# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('name')
        subject = request.POST.get('name')
        message = request.POST.get('name')
        date = request.POST.get('name')
        mycontact = Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
        mycontact.save()
    
    return render(request, "index.html")


