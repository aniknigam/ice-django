from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

def index(request):
    variable = {
        'render': 'show this content',
    }
    return render(request , 'index.html', variable)

def about(request):
    return render(request , 'about.html') 

def services(request):
    return render( request , 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email'] 
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

    return render(request , 'contact.html')