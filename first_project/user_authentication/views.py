from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def code(request):
    return HttpResponse('<h1>This Code is 12345</h1>')
