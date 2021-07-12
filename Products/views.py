from django.shortcuts import render
from django.http import HttpResponse, request
from os import name
from .models import products

# Create your views here.
def index(request):
    param = products.objects.all()
    return render(request, 'products/homepage.html', {'param':param})
