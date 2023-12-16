from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def list(request):
    return HttpResponse('<h1>This is list Page</h1>')