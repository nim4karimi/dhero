from django.shortcuts import render
from django.http import HttpResponse

# Function of polls index

def index(request):
    return HttpResponse("نظر سنجی : ")
