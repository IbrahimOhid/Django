from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def name(request):
    return HttpResponse('<h1>I am Mohammad  Ibrahim</h1>')

def learn(request):
    return HttpResponse('<h1>I Learn Django</h1>')
