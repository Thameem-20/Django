from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"Thameem"
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return HttpResponse('This is services')\

def contact(request):
    return render(request, 'contact.html')
    