from urllib import request
from django.shortcuts import render

# Create your views here.

def HomeView(request):
  return render (request, 'index.html')

def HomePrincipal(request):
  return render (request, 'home-principal.html')

def CorporativeView(request):
  company_data = {
    "social_reason": "Tecnología",
    "direction": "Rosario Norte #2346",
    "contact": "someEmployee@company.cl"
  }
  return render (request, 'corporative.html', company_data)
