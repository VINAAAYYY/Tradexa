from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from os import name

# Create your views here.
def index(request):
    return redirect('/user')