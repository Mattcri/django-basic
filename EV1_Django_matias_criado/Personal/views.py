from django.shortcuts import render

# Create your views here.

def PersonalView(request):
  employeeData = {
    "name": "Matias",
    "lastname": "Criado",
    "email": "mcriado@company.cl",
    "date_birth": "15 de marzo del 1996",
    "age": "26",
    "direction": "Av. Santa María #456, Maipú"
  }
  return render (request, 'personal.html', employeeData)