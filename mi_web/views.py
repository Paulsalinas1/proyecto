from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'vet/index.html')

def tienda(request):
    return render(request,'vet/tienda.html')
