from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    return HttpResponse("welcome to emobilis")
def about(request):
    return HttpResponse("about emobilis")