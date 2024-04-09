from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage/homepage.html')

def login(request):
    return render(request, 'index.html', context={
        "title": "Admin Login"
    })
