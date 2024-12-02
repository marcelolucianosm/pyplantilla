from django.shortcuts import render

# Create your views here.

def home(request):
    contexto = {}
    return render(request, "index.html", contexto)